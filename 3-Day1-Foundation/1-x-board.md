### MicroPythonを走らせられるボード
手に入りやすいボード、商品体系で分けると
| 種類             | 代表ボード                            | 特徴                                     | 用途例          |
| -------------- | -------------------------------- | -------------------------------------- | ------------ |
| Raspberry Pi 系 | Pico / Pico W / Pico 2 W         | 安価で小型、WはWi-Fi内蔵、Armコア  <br> Pico 2は、Arm Cortex-M33 ×2 と RISC-V Hazard3 ×2のデュアルコア構成       | センサー制御、IoT   |
| Arduino 系      | Arduino Uno / Nano / Nano 33 BLE | 豊富なシールド、C/C++中心だがMicroPythonも対応可能      | ロボット、教育      |
| ESP 系          | ESP32 / ESP8266                  | Wi-Fi/Bluetooth内蔵、安価<br> マイコンコアはXtensa | IoT、スマート家電   |
| STM32 系        | Nucleo / Blue Pill               | 高性能Arm Cortex-M、ピン数多め                  | モーター制御、高精度計測 |
| 教育・学習向け        | micro:bit                   | LEDやボタン内蔵、簡単にプログラム可能                   | 初学者、学校教育     |

MicroPythonが対応しているマイコンボード一覧<br>
https://micropython.org/download/

- マイコン基礎（簡単なブロック図、有名なマイコン紹介）
   -  EPS32/ESP32-S2/ESP32-S3 (Tensilica Xtensa Core)
      - 高性能だが消費電力が大きい、WiFiモジュール込みのパッケージ、省サイズ化可能
   -  EPS32-C3/ESP32-C5 (RISC-V Core)
      - ESP32より性能低いがRISC-Vコアを使える WiFiモジュール込みパッケージ
   -  Raspberry Pi Pico 2 (ARM Core/ マイコン名はRP2350)
      - WiFiモジュールは外付け(RP2350はコアと周辺IOのみ)、ESP32より省電力、サイズはやや大、ARM Coreアーキ (RP2450はRISC-Vも内蔵)
   -  STM32系(ボード名：Nucleo)
   -  SAMD系(ARM Cortex-M4Fコア Microchip ATSAMD51P19)(商品 Wio Terminal)
   -  Arduinoもある(Arduinoはマイコンボードであり、開発環境であり、プログラミング言語である)


### どのボードを選ぶか？選び方
- 価格
- ボードのサイズ
- 使えるPinの数
- WiFiが搭載されているか
- BLEが搭載されているか
- RAMのサイズ、Flashのサイズ
- 使われているマイコンコアのアーキテクチャ、システムクロック
- 表示用デバイスが搭載されているか
- センサ類が搭載されているか（カメラ搭載型もあり）
- ケースに入っているか
