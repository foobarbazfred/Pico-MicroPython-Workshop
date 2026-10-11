# ボードへの電源供給について

### 電源供給方法

ボードを動かすための電源供給方法として、大きく分けて（１）USBから供給、（２）電池から供給が挙げられます。
#### USBから電源供給
- USBとボードを接続した場合、USBケーブルから５Vが供給され、ボード内で3.3Vに変換されます。
- USBから供給されている５Vを40番ピン(VBUS)から取り出して周辺デバイスに供給することができます。
- VSYSを使って周辺デバイスに電源供給することも可能ですが、この場合、ショットキーダイオード(D1)を介するため電圧が少し下がる点に注意が必要です。
- 仕様書には、USBからのみ電源供給する場合、VBUSとVSYSを直結することで、ショットキーダイオード(D1)をバイパスさせる方法が提案されています。ダイオードをバイパスさせることで、電力ロスを少しでも回避させるという案です。一方、ダイオードは、VSYSからUSBへの電源流入を防ぐ保護回路の働きですのでバイパスさせることで、保護回路が無効化されます。誤ってVSYSに電源を接続しないように注意が必要です。

#### 電池から電源供給の場合
- 電池駆動の場合、接続は39番ピンのVSYSに電源を供給します。
- ボードにはSMPS（昇降圧レギュレータ）が搭載されており、1.8Vから　5.5Vまでの電圧であれば、3.3Vに正しく変換されボードが起動されます。

<img width="855" height="359" alt="image" src="https://github.com/user-attachments/assets/71408a11-6242-4b92-adc5-d4b514254740" />

「Raspberry Pi Pico 2 W Datasheet An RP2350-based microcontroller board with wireless」3.4. Powerchainより引用

VSYSから電源として入力できる最大電圧が5.5Vなので、電池駆動の場合、この電圧（定格）を超えないよう注意が必要です。

<img width="1357" height="1116" alt="image" src="https://github.com/user-attachments/assets/64de529b-32d4-4ec9-9c9a-3040937bb610" />

Figure 2. The pinout of the Pico 2 W board　　1. About Pico 2 W　より引用

### 参考文献
1. [Raspberry Pi Pico 2 W Datasheet An RP2350-based microcontroller board with wireless](https://pip.raspberrypi.com/documents/RP-008304-DS)
