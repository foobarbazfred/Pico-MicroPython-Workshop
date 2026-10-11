# ボードの使い方

### 電源供給方法

ボードを動かすための電源供給方法として、大きく分けて（１）USBからの供給、（２）電池駆動での供給が挙げられます。
#### USBからの電源供給
USBとボードを接続した場合、USBケーブルから５Vが供給され、ボード内で3.3Vに変換されます。また、周辺デバイスにUSBから供給されている５Vを40番ピン(VBUS)から取り出して供給することができます。
#### 電池からの電源供給の場合
電池駆動の場合、接続は39番ピンのVSYSに電源を供給します。ボードには＃＃＃が搭載されており、1.8Vから　5.5Vまでの電圧であれば、＃＃＃に昇降され、＃＃＃＃されます。

<img width="855" height="359" alt="image" src="https://github.com/user-attachments/assets/71408a11-6242-4b92-adc5-d4b514254740" />

「Raspberry Pi Pico 2 W Datasheet An RP2350-based microcontroller board with wireless」3.4. Powerchainより引用

電源として入力できる最大電圧が5.5Vなので、電池駆動の場合、この電圧（定格）を超えないように注意が必要です。
