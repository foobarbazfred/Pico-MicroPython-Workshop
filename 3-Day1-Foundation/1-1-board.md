### 手に入りやすいボード、商品体系
Linux等は動かず、OSなしでアプリケーションを稼働させる小規模なマイコンボードを整理しました。
| 種類             | 代表ボード                            | 特徴                                     | 用途例          |
| -------------- | -------------------------------- | -------------------------------------- | ------------ |
| Raspberry Pi 系 | Pico / Pico W / Pico 2 / Pico 2 W | 安価で小型、WはWi-Fi内蔵、Armコア  <br> Pico 2は、Arm Cortex-M33 ×2 と RISC-V Hazard3 ×2のデュアルコア構成       | センサー制御、IoT   |
| Arduino 系      | Arduino Uno / Nano / Nano 33 BLE | 豊富なシールド、C/C++中心だがMicroPythonも対応可能(Nano 33 BLEのみ)      | ロボット、教育      |
| ESP 系          | ESP32 / ESP8266                  | Wi-Fi/Bluetooth内蔵、安価<br> マイコンコアはXtensa | IoT、スマート家電   |
| STM32 系        | Nucleo / Blue Pill               | 高性能Arm Cortex-M、ピン数多め                  | モーター制御、高精度計測 |
| 教育・学習向け        | micro:bit                   | LEDやボタン内蔵、簡単にプログラム可能                   | 初学者、学校教育     |

### MicroPythonが対応しているマイコンボード
https://micropython.org/download/
- 商品体系別
   -  EPS32/ESP32-S2/ESP32-S3 (Tensilica Xtensa Core)(商品名：M5Stack / M5Stampシリーズ)
      - 高性能だが消費電力が大きい、Wi-Fiモジュール込みのパッケージ、省サイズ化可能
   -  EPS32-C3/ESP32-C5 (RISC-V Core)
      - ESP32より性能低いがRISC-Vコアを使える WiFiモジュール込みパッケージ
   -  Raspberry Pi Pico シリーズ (ARM Cortex-M/ マイコン名はRP2350) (Pico Pico W, Pico 2, Pico 2 W いずれも稼働）
      - WiFiモジュールは外付け(RP2350はコアと周辺IOのみ)、ESP32より省電力、ボードサイズはやや大きい、ARM cortex-M (RP2450はRISC-Vも内蔵)
      - Picoシリーズ以外でRP2350を使った省サイズボードもある
   -  STM32系(ARM Cortex-M)(ボード名：Nucleo)
   -  SAMD系(ARM Cortex-M4Fコア Microchip ATSAMD51P19)(商品名：Wio Terminal)
   -  micro:bit(ARM Cortex-M)
   -  Arduinoもある(Arduinoはマイコンボードであり、開発環境であり、プログラミング言語である)（ボード名：Nano 33 BLEはMicroPython稼働）

### どのボードを選ぶか？選び方
- 価格
- ボードのサイズ
- 使えるPinの数
- 無線機能の有無
   - Wi-Fiが搭載されているか
   - BLEが搭載されているか
   - その他(Rola, )
- RAMのサイズ、Flashのサイズ
- 使われているマイコンコアのアーキテクチャ、システムクロック
  - コアの種類（ARM(Cortex-M)、RISC-V, Xtensa, etc） 
- 表示用デバイスが搭載されているか
- センサが搭載されているか（カメラ搭載型もあり）
- ケースに入っているか
- 電源系統の仕様
   - 充電機能がついているか（リチウムイオン電池への充電機能）
   - 電池ホルダ付きか（単３、単４駆動）

コアの種類が何であるかについて、MicroPythonを使う上では抽象化（隠蔽）されているため、アプリケーション開発においてソフトへの影響はほとんどありません。一方で、MicroPythonをカスタマイズするためMicroPython自体のビルドが必要になった時、ターゲットとするコアのアーキテクチャによって必要なコンパイラやSDKなどのビルドツールが異なります。どのコアを使うかにより、ビルドの難易度や入手できる情報量も変わってくると思われます。
