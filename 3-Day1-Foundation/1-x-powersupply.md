# ボードへの電源供給について

### 電源供給方法
ボードを動かすための電源供給方法として、大きく分けて（１）USBから供給、（２）電池から供給が挙げられます。

### USBから電源供給の場合
* USBとボードを接続した場合、USBケーブルから5Vが供給され、ボード内で昇降圧レギュレータ（SMPS）によりマイコン電源用の3.3Vに変換されてボードが起動します。
* USBからの5V電源は、**40番ピン(VBUS)**から取り出して周辺デバイスに供給することができます。
* **39番ピン(VSYS)**を使って周辺デバイスに電源供給することも可能ですが、内部のショットキーダイオード(D1)を通るため、電圧が少し低下する点に注意が必要です(一般的に、0.3V程度低下)。
* レギュレータで電圧補正された3.3Vが**36番ピン(3V3)**に出力されます。3.3Vで動作するセンサー等に給電する場合は、36番ピン(3V3 OUT)の3.3Vを使用します。
* 仕様書では、USB給電のみで運用する場合にVBUSとVSYSを直結してダイオード(D1)をバイパスさせる手法も紹介されています。ダイオードによる電圧降下をなくすことで、電源効率の向上や電圧リップル（ノイズ）の低減が図れます。
* ただし、バイパスさせると逆流防止の保護回路が無効化されます。直結した状態でVSYSに外部電源を接続すると、接続しているPCなどのUSB機器を破損させる恐れがあるため注意してください。

### 電池から電源供給の場合
* 電池駆動の場合、電源は**39番ピン(VSYS)**に接続します。
* ボードには昇降圧レギュレータ（SMPS）が搭載されています。入力電圧が1.8V〜5.5Vの範囲内であれば、マイコン電源用の3.3Vに変換されてボードが起動します。
* 電池駆動の際は、VSYSへの入力電圧が許容上限（5.5V）を超えないよう注意が必要です。
* レギュレータで電圧補正された3.3Vが**36番ピン(3V3)**に出力されます。3.3Vで動作するセンサー等に給電する場合は、36番ピン(3V3 OUT)の3.3Vを使用します。

<img width="855" height="359" alt="image" src="https://github.com/user-attachments/assets/71408a11-6242-4b92-adc5-d4b514254740" />
[1] Raspberry Pi Pico 2 W Datasheet ; 3.4. Powerchainより引用


<img width="1357" height="1116" alt="image" src="https://github.com/user-attachments/assets/64de529b-32d4-4ec9-9c9a-3040937bb610" />

Figure 2. The pinout of the Pico 2 W board  / [1]Raspberry Pi Pico 2 W Datasheet; 1. About Pico 2 W　より引用

### 参考文献

電源の接続方法について詳しくは、[1]Raspberry Pi Pico 2 W Datasheetの、3.4. Powerchainの章を参照してください。充電池の接続説明もあります（Using a battery charger）。

1. [Raspberry Pi Pico 2 W Datasheet An RP2350-based microcontroller board with wireless](https://pip.raspberrypi.com/documents/RP-008304-DS)
