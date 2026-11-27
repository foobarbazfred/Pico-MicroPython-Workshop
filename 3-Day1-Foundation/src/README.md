# src ディレクトリのファイル一覧

Raspberry Pi Pico / Pico 2 と MicroPython を使った、Day 1 Foundation のサンプルプログラムと補助ファイルです。センサ、ディスプレイ、カメラ、ネットワークなどの動作例を収録しています。

## サンプルプログラム

| ファイル | 機能概要 |
| --- | --- |
| `2-2-f-blink.py` | 外付けスイッチの入力を読み取り、LEDを点灯・消灯します。スイッチの値もコンソールに表示します。 |
| `2-3-f-simple-blink.py` | 基板上のBOOTSELボタンの状態に応じて、基板上のLEDを点灯・消灯します。 |
| `2-4-f-adc-sample.py` | GP26のADCでボリュームの電圧を読み取り、ADC値と推定電圧を表示します。 |
| `2-7-f-beep-by-pwm.py` | PWM周波数を変化させ、圧電サウンダから音を鳴らします。 |
| `2-9-ex-neopixel-rotate.py` | 8個のNeoPixelの点灯位置を順番に移動させ、回転するような光の演出を行います。 |
| `3-6-f-co2-sensor.py` | SCD41からCO₂濃度・温度・湿度を読み取り、コンソールに表示します。 |
| `3-7-f-motion-sensor.py` | MPU6050から加速度と角速度を読み取り、スケール換算した値を表示します。 |
| `3-7-ex-motion-lcd.py` | MPU6050の加速度・角速度を読み取り、加速度をコンソールとI2C LCDに表示します。 |
| `3-8-f-distance-sensor.py` | HC-SR04で距離とエコーパルス幅を測定し、コンソールに表示します。 |
| `3-8-ex-distance-lcd.py` | HC-SR04で測定した距離とパルス幅をコンソールおよびLCDに表示します。 |
| `3-9-f-pir-sensor.py` | PaPIRs人感センサの出力を読み取り、人の検知状態を表示します。 |
| `3-10-gps_gt-502.py` | GT-502GG GPS受信機のNMEAデータをUARTで受信・解析し、時刻や位置情報をLCDに表示します。 |
| `3-11-f-arducam-sample.py` | Arducam OV5642で撮影し、画像データをバッファに読み込みます。 |
| `3-11-ex-arducam-lcd.py` | Arducam OV5642で撮影した画像をST7735グラフィックLCDに表示します。 |
| `3-20-f-lcd-display.py` | I2C接続の16×2キャラクタLCDを初期化し、文字列を表示します。 |
| `3-21-f-graphic-display.py` | ST7735グラフィックLCDに色、図形、テキストを描画します。 |
| `rfid_test.py` | MFRC522リーダーでRFIDカードを検出し、カード種別・UIDの読み取りやメモリ読み出しを試します。 |
| `boot.py` | 起動時にWi-Fiへ接続し、接続成功後にNTPでシステム時刻を同期します。Wi-Fiの認証情報を設定して使用します。 |

## ライブラリ (`lib/`)

サンプルプログラムから読み込まれるドライバ、共通処理、実験用コードです。

| ファイル | 機能概要 |
| --- | --- |
| `I2C_LCD.py` | PCF8574経由でHD44780互換キャラクタLCDを制御するI2C実装です。 |
| `LCD_API.py` | キャラクタLCDの初期化、カーソル、表示、文字出力などの共通APIです。 |
| `hc_sr04.py` | HC-SR04超音波距離センサのトリガー出力、エコー測定、距離計算を行うドライバです。 |
| `mfrc522.py` | MFRC522 RFIDリーダーの通信、カード検出、認証、読み書きを行うドライバです。 |
| `mpu6050.py` | MPU6050の初期化と加速度・角速度データの読み取りを行うドライバです。 |
| `mylib.py` | PWMサーボの角度指定をパルス幅に変換する関数を提供します。 |
| `neopixel.py` | RP2040 PIOを使ってWS2812/NeoPixel LEDを制御するクラスを提供します。 |
| `ov5642.py` | OV5642カメラのレジスタ設定、撮影設定、画像読み取りを行うドライバです。 |
| `ov5642_FIFO.py` | Arducam FIFOの撮影制御、レジスタアクセス、画像データ読み取りを行います。 |
| `ov5642_setup.py` | OV5642のプレビューおよびRGB565出力に使うレジスタ設定値を定義します。 |
| `scd41.py` | SCD41の周期測定制御と、CO₂濃度・温度・湿度の読み取りを行うドライバです。 |
| `upysh2.py` | MicroPython上でファイル一覧、移動、コピー、削除などを行う簡易シェル関数を提供します。 |
| `I2S_sample.py` | I2S出力の接続確認用サンプルです。波形データを生成して出力します。 |
| `I2S_sample2.py` | MAX98357向けに符号付き16bitの正弦波を生成し、I2Sで連続再生するサンプルです。 |
| `I2S_sample3.py` | I2Sで正弦波音を出力する実験用サンプルです。 |
| `I2S_sample4.py` | 音量を変化させながら符号付き16bit正弦波をI2S出力する実験用サンプルです。 |

## Webサーバ (`web_server/`)

| ファイル | 機能概要 |
| --- | --- |
| `rp2_webserver.py` | Pico 2 W上でHTTPサーバを起動し、GPIO・LED・BOOTSELボタンの状態表示と、WebページからのLED/GPIO切り替えを行います。 |

## MQTTダッシュボード (`mqtt_dashboard/`)

| ファイル | 機能概要 |
| --- | --- |
| `client_sample_pc.py` | PCからMQTTブローカーへランダムな値をJSONで定期送信するデモクライアントです。 |
| `client_sample_voltage.py` | 0〜3.3 Vの電圧を模した値を生成し、HiveMQのMQTTトピックへ定期送信します。 |
| `dashboard.html` | MQTT over WebSocketで値を受信し、ユーザーごとの値をドーナツチャートで表示するWebダッシュボードです。 |
| `dashboard_nicegui.py` | MQTTで受信した電圧をNiceGUIでゲージと時系列グラフに表示します。 |
| `node_red_iot_dashboard_flows.json` | MQTTから電圧データを取得し、ゲージやチャートに表示するNode-REDフローです。 |
| `prompt_memo.txt` | MQTTダッシュボード作成に関するメモです。 |
| `simple_IoT_dashboard.png` | IoTダッシュボードの画像資料です。 |

## 実行時の注意

- これらはMicroPython対応ボード向けの学習用サンプルです。対象ボード、配線、センサ、LCDの種類に合わせてGPIO番号やI2C/SPI/UART設定を確認してください。
- `lib/` 内のモジュールをサンプルから利用する場合は、ボード上でインポートできる場所（通常は `lib/` またはルート）に配置してください。
- MQTTのサンプルには外部ブローカーや追加ライブラリ（例: PC側の `paho-mqtt`、`dashboard_nicegui.py` の `nicegui`）が必要です。トピック名やブローカー設定は利用環境に合わせてください。
- `boot.py` の `SSID` と `PASSWD` は、使用するWi-Fiの情報に変更してください。
