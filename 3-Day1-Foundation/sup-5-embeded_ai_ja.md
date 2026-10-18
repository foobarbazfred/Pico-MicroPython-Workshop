# 生成AIと組み込みアプリの連携（Web API と TFLM にフォーカス）

## 概要
本稿は「組み込みアプリ（マイコン）に LLM / 生成AI をどのように連携できるか」に特化して整理した解説です。特に実務的に現実的な以下二つの方法に焦点を当てます。

1. Web API（クラウド／エッジの LLM）を呼び出す方式
2. TensorFlow Lite for Microcontrollers（TFLM）などの軽量モデルをアプリに組み込む方式

多くのケースで実用的な解は両者を組み合わせたハイブリッドになります。端末側は軽量判定や特徴抽出を行い、生成や長文説明など重い処理は外部 LLM に委ねます。

---

## 先に結論（要点）
- 実装パターンは大きく「オンデバイス小モデル + クラウドLLM（標準）」「エッジサーバ配置」「限定的オンデバイス」「フェールセーフ」の4種
- Web API 呼び出しは柔軟で強力だが、遅延・コスト・プライバシーのトレードオフがある
- TFLM 等はオンデバイスでのリアルタイム判定に有効で、LLM 呼び出しのトリガーとして最適
- まずは「端末で閾値判定/意図判別→ 必要時に LLM 呼び出し（RAG を含む）」の試作から始めるのが現実的

---

## 代表的アーキテクチャパターン

### パターンA：オンデバイス小モデル + クラウドLLM（標準ハイブリッド）
- 端末: ウェイクワード検知、意図分類、特徴量抽出（TFLM 等）
- 通信: MQTT / HTTPS で要約や特徴量を送信
- サーバ: LLM API（OpenAI 等）で生成、必要に応じてベクトル検索
- 利点: 低消費電力・即時応答。複雑処理はサーバ任せ
- 注意: 通信依存、遅延、ランニングコスト、プライバシー

### パターンB：エッジサーバ（オンプレ近接）
- 端末は軽量前処理のみ。生成や大きめのモデルは近接エッジサーバで実行
- 利点: 公衆網を経由せずレイテンシ・プライバシー面で有利

### パターンC：限定的オンデバイス（MCU 限定）
- MCU 上ではキーワード検出や簡易分類など小さな NN を実行
- Raspberry Pi 等の SBC ならローカルでより大きなモデル（Llama.cpp 等）を動かせる場合あり

### パターンD：ハイブリッド・フェールセーフ
- 通常は端末判定。信頼度低または詳細化が必要なときのみ LLM へ問い合わせ
- ネットワーク断時はローカルの閾値判定／事前定義応答へフォールバック

---

## Web API 呼び出し方式（設計と実装のポイント）

### 何を送るか（データを最小化する）
- 生データ（長い音声やフル解像度画像）は原則送らない
- 端末で要約・抽出した特徴量や短いサマリ、メタデータを送る
- 例: { device_id, timestamp, summary: "vibration high for 20s", features: { rms: 1.23, peak: 2.5 }, model_hash }

### 通信方式の選択
- 即時対話: WebSocket（双方向）、HTTP(S) ストリーミング
- バッチ解析: MQTT / HTTPS（バッチ送信）

### 認証とセキュリティ
- TLS（HTTPS）必須。API キーは secure element / provisioning を使って安全に管理
- リクエストに request_id, model_id を付与し、レスポンスと突合
- プロンプト・レスポンス・モデルバージョンは監査ログへ保存

### レイテンシ対策
- 端末で簡易判定（閾値／意図分類）→ 必要時のみ API 呼び出し
- ストリーミング応答で最初の断片を早めに返す設計

### コスト対策
- 送信データの圧縮・要約、問い合わせのバッチ化
- 同一プロンプトのキャッシュ

### 再試行・レート制御
- Exponential backoff、キューイング、ローカルバッファによる再送

### MicroPython からの概念的な POST 例
```python
# MicroPython の簡易例（実運用では TLS 検証やキー管理が必要）
import urequests, ujson
url = "https://api.example-llm.com/v1/generate"
headers = {"Authorization":"Bearer YOUR_API_KEY","Content-Type":"application/json"}
payload = {
  "device_id": "dev-001",
  "timestamp": 1680000000,
  "summary": "vibration high for 20s, temp 75C",
  "features": {"rms":1.23, "peak":2.5}
}
res = urequests.post(url, headers=headers, data=ujson.dumps(payload))
if res.status_code == 200:
  body = res.json()
  print("response:", body.get("text"))
else:
  # ローカルフォールバック処理
  print("error", res.status_code)
res.close()
```

---

## TFLM（TensorFlow Lite for Microcontrollers）を組み込む方法

### 全体手順（要点）
1. モデル設計・学習（PC 上で学習。Edge Impulse や TensorFlow を利用）
2. 量子化（post-training quantization）でサイズと推論コストを削減
3. saved_model → tflite に変換
4. tflite バイナリを MCU に組み込む（xxd -i で C 配列に変換するなど）
5. TFLM ランタイムをファームウェアに組み込み、tensor_arena サイズを最適化
6. 実機でメモリ・パフォーマンスを評価し調整

### 実装上の注意点
- tensor_arena のサイズは慎重に決定（小さすぎると Allocate に失敗）
- プルーニングや蒸留でさらにモデルを小型化
- 実行は割り込みや他処理と競合しないようスケジューリングする

### TFLM による典型的処理（C の概念例）
```c
#include "tensorflow/lite/micro/all_ops_resolver.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "model_data.h" // tflite を C 配列へ変換したヘッダ

constexpr int kArenaSize = 16 * 1024;
static uint8_t tensor_arena[kArenaSize];

void run_inference(float* input_data, size_t input_len) {
  tflite::AllOpsResolver resolver;
  tflite::MicroInterpreter interpreter(model, resolver, tensor_arena, kArenaSize, &micro_error_reporter);
  interpreter.AllocateTensors();
  float* input = interpreter.input(0)->data.f;
  // copy input_data -> input
  interpreter.Invoke();
  float* output = interpreter.output(0)->data.f;
  // output を使って閾値判定やスコア化
}
```

---

## ミニマムな ML を組み込む用途（TFLM に向くもの）
- キーワード検出（keyword spotting）
- 簡易意図分類（音声/テキストの小分類）
- 異常検知（時系列の簡易モデルや統計特徴量に基づく判定）
- センサデータの特徴抽出（後段 LLM に渡すための要約）

これらは MCU レベルで十分に動作することが多く、生成AI 呼び出しのトリガーや事前フィルタとして最適です。

---

## 組み込みアプリとして作れるアプリケーション例
- 音声操作デバイス：ウェイクワード → 意図分類（端末）→ 複雑対話は LLM に委任
- 機器の自然言語状態報告：センサ特徴量を送信 → LLM が報告文と対処案を生成
- 異常検知＋レポート自動生成：TFLM で検知 → ログ要約を送信 → LLM がレポートを生成
- 設定支援インタフェース：自然言語での設定要求を LLM でパラメータ化 → 端末へ配布
- 過去ログ検索＋説明：埋め込み DB を使った類似ログ検索 → LLM が説明を生成

---

## データフロー設計の実務ポイント
- 端末は原則「要約・特徴量のみ」を送信（生データは必要時のみ）
- プロンプトは構造化テンプレート（facts + question）を用意して安定化
- 全問い合わせに request_id、model_version、prompt_hash を含め監査ログ保存
- 同一問い合わせはキャッシュして API 負荷を軽減

---

## セキュリティ・プライバシー・ガバナンス
- 機密データは匿名化/集計するかオンデバイスで処理する
- API キーや秘密情報は secure element 等を使い安全に保管
- 外部 LLM を利用する場合、データ利用条件（DPA）・保持方針を確認
- 生成結果は "提案" として扱い、重要な操作は人の承認を必須化
- 生成コードは必ず SAST/静的解析とレビューを通す

---

## 実装上のよくある問題と対策
- hallucination（誤生成）: 事実ベース DB と組合せた RAG（Retrieval-Augmented Generation）で対策
- レイテンシが長い: 部分応答（streaming）や先に簡易応答を端末で返す設計
- メモリ不足: モデルをさらに小型化、tensor_arena の調整、より小さい演算単位で分割

---

## 短期プロトタイプ（試作）手順
1. ユースケース決定（例: 異常検知→自然言語レポート生成）
2. 端末で抽出する最小特徴量を設計し、TFLM モデルを作成・検証
3. 小さな LLM エンドポイント（クラウド/エッジ）を作り、構造化プロンプトで試す
4. セキュリティ（TLS・キー管理）とフォールバックを実装
5. 評価（レイテンシ・通信量・誤検知・コスト）

---

## 推奨スタートポイント
1. まずは TFLM による閾値判定／意図分類を端末で実装
2. 必要時に LLM を叩くフローを追加（まずは非ストリーミングの簡単な API 呼び出し）
3. 効果を定量化し、次に RAG やストリーミングを検討

---

## 参考リンク
- TensorFlow Lite for Microcontrollers: https://www.tensorflow.org/lite/microcontrollers
- Edge Impulse: https://www.edgeimpulse.com/
- OpenAI API: https://platform.openai.com/
- Llama.cpp / ggml（ローカル推論の参考）

---

## 次のアクション（提案）
- A) この MD をリポジトリへコミットする（ファイル名: 3-Day1-Foundation/sup-5-embeded_ai_ja.md）
- B) 特定デバイス（例: Pico W / RP2040 / ESP32）向けにサンプルコード（MicroPython）と TFLM の最小例を作る
- C) 具体ユースケースを1つ選んで E2E のサンプル（端末: TFLM、サーバ: LLM 呼び出し、評価指標）を作る

希望するアクションを教えてください。
