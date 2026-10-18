# マイコンとAIの連携（改訂版）

## はじめに
Raspberry Pi Pico 系などのマイコン（例：Pico 2 W 等、チップは一般に RP2040 系）とAIを組み合わせることで、従来クラウドに頼っていた処理をエッジ側で低遅延・省電力に実現できます。本稿は組み込みアプリ開発におけるAI連携の実践的な注意点、手順、ハンズオン例、運用面（モデル更新・監視・セキュリティ）までを整理した改訂版です。

> 注: リファレンス文書や README に特定ボード名がある場合は、チップ名（例: RP2040）やボード名（Pico W / Pico 2 W）を正確に確認してください。本稿では一般的な制約と手法を示します。

---

## 本稿で扱う主題
- オンデバイス（端末内）推論とクラウド推論の使い分け
- 非機能要件の定量化と判断基準（レイテンシ、消費電力、メモリ）
- モデル軽量化（量子化・蒸留）・ツールの使い分け
- 実機でのベンチマーク方法（レイテンシ、メモリ、消費電力）
- ハンズオン（データ収集 → モデル作成 → TFLite 変換 → デプロイ）具体例
- 運用（OTA・署名・バージョン管理・監視）とセキュリティ
- 用語集（Glossary）と参考リンク

---

## 1) オンデバイス vs クラウド — 判断基準
用途や制約に応じて選ぶ。代表的な判断基準は以下。

- レイテンシが重要（例：200 ms 未満） → オンデバイスを検討
- プライバシー重視（個人情報を外送したくない） → オンデバイス優先
- モデルサイズ・計算量が大きく精度が重要 → クラウド（またはハイブリッド）
- 常時動作でバッテリ重視 → 省電力設計（間欠評価、wake-word 前処理）

ハイブリッド戦略例：ウェイクワードや前処理は端末、重い推論はクラウドで実施。

---

## 2) 非機能要件（必ず定量化する）
設計の最初に必ず数値を決める。例：

- レイテンシ: 応答 200 ms 以下
- メモリ: RAM 実効 256 KB、使用可能ヒープ 64 KB（例）
- ストレージ: Flash 2 MB 利用可能
- 消費電力: 待機時 < 1 mA、ピーク推論時 < 50 mA（目安）
- バッテリ要件: 24 時間連続稼働

上記はボード・用途によって大きく異なるため、実機での測定が必須です。

---

## 3) モデル軽量化の具体手法
オンデバイスでの実行を可能にする代表的な技術とポイント。

- 量子化（Quantization）
  - Post-training quantization（例: int8 の重みとアクティベーション）
  - Quantization-aware training（QAT）で精度低下を抑える
  - 効果: モデルサイズ縮小、推論速度向上、メモリ縮小

- 蒸留（Knowledge Distillation）
  - 大きいモデル（teacher）から小さいモデル（student）へ知識を移す
  - 小型モデルでの精度向上に有効

- ネットワーク設計の工夫
  - Depthwise separable conv、軽量化アーキテクチャ（MobileNet 系など）
  - 入力解像度・フレームレートの低下による前処理

- さらに
  - 重みの剪定（pruning）、ハフマン符号化などの圧縮

---

## 4) 推論ライブラリ・ツール比較（短評）
- TensorFlow Lite: モバイル・サーバー向け（比較的大きなランタイム）
- TensorFlow Lite Micro (TFLM): マイコン向け（RTOS / no-OS でも動く軽量ランタイム）
- Edge Impulse: データ収集〜学習〜デプロイま��を支援するプラットフォーム（組み込み向けに最適化）
- TinyML: 取り組み領域の総称・コミュニティ（TFLM や CMSIS-NN を利用）
- ulab: MicroPython 上での数値処理ライブラリ

選択のポイント: 実行対象（MCU の RAM/Flash）、モデルフォーマット（TFLite）、使用言語（MicroPython/C/C++）を基準に選ぶ。

---

## 5) 実機ベンチマーク（推奨手順）
簡易かつ実用的な測定方法を示します。

1) レイテンシ計測
   - 手法A（GPIO トグル法）: 推論開始直前に GPIO を high、終了後に low にし、オシロ／ロジアナでパルス幅を測定。
   - 手法B（シリアルタイムスタンプ）: 推論前後にミリ秒単位のタイムスタンプをシリアル出力して差をとる（注意: シリアル自体が遅延を生む）。

2) メモリ使用量
   - MicroPython: gc.mem_free() / gc.mem_alloc() を使った前後比較
   - C/C++ (TFLM): 実行バイナリ内の heap 使用量測定（デバッグ用ログ）、使用ピークを確認

3) 消費電力
   - 電源ラインに小型電流センサ（例: INA219）を挿入して測定
   - USB 電流計やログ記録機能で待機/処理時の電流を比較

4) 持続評価
   - 実際のワークロードでの長時間動作（例: 24 時間）でメモリリークや精度劣化を観察

---

## 6) ハンズオン例: 温度/振動による異常検知（簡易フロー）
以下は最短プロトタイプ手順の例です。

前提: Python 環境 (3.8+)、TensorFlow (または Edge Impulse)、Raspberry Pi または開発 PC

1) データ収集
   - 実機で正常/異常データを収集し CSV に保存
   - サンプリング周波数、ウィンドウサイズを確定（例: 100Hz、1秒=100サンプル）

2) 前処理 & 特徴量
   - 窓化 → 正規化 → 平均・標準偏差・FFT の主要係数などを抽出

3) モデル作成（PC 上）
   - 軽量な CNN または全結合ネットワークで検証
   - 精度が取れたら量子化を適用（post-training quantization）

例: TFLite への変換（Python スクリプト）
```bash
# TensorFlow model -> TFLite (post-training quantization の例)
python - <<'PY'
import tensorflow as tf
model = tf.keras.models.load_model('model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
# 量子化用の代表入力関数を用意すると、int8 量子化が可能
# converter.representative_dataset = representative_dataset_gen
# converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
# converter.inference_input_type = tf.uint8
# converter.inference_output_type = tf.uint8
tflite_model = converter.convert()
open('model.tflite','wb').write(tflite_model)
PY
```

4) TFLite Micro 向け準備と MicroPython 側での呼び出し（擬似コード）
- 多くの場合、TFLM を C++ 側でビルドして MicroPython に組み込むか、既存のラッパーを使います。
- 擬似 MicroPython 呼び出し例:
```python
# pseudo-code
from tflite_wrapper import load_model, run_inference
model = load_model('/models/model.tflite')
input = get_windowed_sensor_data()
output = run_inference(model, input)
print(output)
```

5) 実機検証
   - レイテンシ／メモリ確認、しきい値調整、誤検知ケースの収集

6) デプロイ
   - モデルをデバイスに配置（Flash / SPIFFS / SD）し、署名検証を入れてから読み込み

---

## 7) 運用: OTA・バージョン管理・ロールバック
運用中にモデルを更新する際の要点:

- モデル署名と検証
  - モデルファイルに HMAC またはデジタル署名を付与し、デバイス側で検証してから反映する

- バージョン管理
  - semantic versioning の採用（例: v1.2.0）
  - モデル内に metadata（training_date, version, input_shape）を埋め込む

- 安全な配布
  - HTTPS + 認証付き API（アクセストークン）で配布
  - 差分配信を利用して帯域を削減

- ロールバック
  - 旧バージョンを保持しておき、異常時にすぐ戻せるようにする
  - Canary デプロイ: 段階的に少数デバイスで試験配信

---

## 8) 監視とドリフト検知
- 監視指標例: 推論成功率、confidence（確信度）分布、入力特徴量の統計（平均/分散）、デバイス毎のエラー率
- ドリフト検知
  - 埋め込み（ベクトル）分布の距離（例: コサイン距離）をモニタリング
  - 入力分布が訓練時と大きく異なる場合は再学習アラートを出す
- ログ送信ポリシー
  - 全データ送信は帯域とプライバシーの問題になるため、要約統計やサンプルのみ送る設計を推奨

---

## 9) セキュリティとプライバシー（実務的対策）
- 機密情報の送信を最小化
  - 個人データは端末で匿名化・集計してから送信する、あるいは端末内処理を優先

- API キー/トークン管理
  - デバイスに平文で置かない。必要に応じてデバイス認証（証明書・相互 TLS）を採用

- モデル・ファイルの署名検証
  - 不正なモデルの配布を防止するため署名検証は必須

- 供給連鎖リスク（SBOM 等）や依存ライブラリの脆弱性管理

---

## 10) ドキュメント構成とメンテナンスの提案
- 役割別ファイル分割
  - sup-5-embedded_ai_ja.md: 技術解説・設計指針（本ファイル）
  - sup-5-ai_assisted_development_ja.md: 生成AI（Copilot 等）を活用した開発ワークフロー
  - hands-on チュートリアル（別ファイル）: 実行コマンド、サンプルデータ、期待出力

- クイックスタート（別ファイル）: 1 ページで最低限の準備と最初のコマンドを示す
- Glossary（用語集）: 重要語の定義を一箇所に置く

---

## 11) 簡易用語集（Glossary）
- On-device / オンデバイス: 端末内部で推論を行うこと
- Quantization / 量子化: 浮動小数点を整数表現に変換してモデルを小型化・高速化する手法
- QAT: Quantization-aware training（量子化を意識した学習）
- TFLite: TensorFlow Lite
- TFLM: TensorFlow Lite Micro（マイコン向けランタイム）
- TinyML: マイコン等の低リソース環境向け機械学習技術の総称

---

## 12) 参考リンク
- TensorFlow Lite Micro: https://www.tensorflow.org/lite/microcontrollers
- Edge Impulse: https://www.edgeimpulse.com/
- TinyML: https://www.tinyml.org/
- ulab (MicroPython 向け数値処理): https://github.com/v923z/micropython-ulab
- CMSIS-NN (ARM 向け高速推論ライブラリ): https://developer.arm.com/開発ツール/CMSIS/CMSIS-NN

---

## 最後に（変更点の要約）
- ファイル名の綴りを "embeded" → "embedded" に修正した新ファイルを作成しました。
- 文字化け・途中切れと思われる箇所を削除・修正し、構成を再整理しました。
- 非機能要件の定量例、量子化や蒸留などの具体的手法、TFLite/TFLM 等のツール差、ベンチマーク手順、OTA/署名/監視・セキュリティの実務的な注意点を追加しました。

必要であれば、このファイルをさらに分割してハンズオン用の手順ファイル（コマンド・サンプルデータ・期待出力を含む）を別途追加で作成します。どの部分を優先して補強しましょうか？
