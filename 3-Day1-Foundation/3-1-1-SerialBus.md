# マイコンとセンサを接続するシリアルインタフェース(I/F)

センサや表示装置との接続は一般的にシリアルI/Fが使用されます。主なシリアルI/Fとして以下が挙げられます
1. UART (クロック信号なし、送信、受信、GNDの３線)(低速)
2. I2C (クロック信号、双方向データ信号、GNDの３線)(低速)
4. SPI (クロック信号、送信、受信、チップセレクト、GNDの5線)(高速転送可能)
5. その他のシリアルI/F
   1. 1-Wire (双方向データ信号、GNDの2線)(低速))
   3. QSPI (SPIをベースとしつつ、データ信号が４本)
   4. I2S (音声データ専用のシリアルインタフェース)

今回の演習ではI2Cを使ってセンサ、表示装置と接続します。


## 参考情報
- MicroPython Documents; RP2 用クイックリファレンス
  - https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#hardware-i2c-bus
- クラスI2C
  - https://micropython-docs-ja.readthedocs.io/ja/latest/library/machine.I2C.html#class-i2c-a-two-wire-serial-protocol
- I2Cバス仕様書 (I2Cバス仕様およびユーザーマニュアル)(NXP)
  - https://www.nxp.com/docs/ja/user-guide/UM10204.pdf
- SPI解説文
  - https://www.ti.com/content/dam/videos/external-videos/en-us/6/3816841626001/6163521589001.mp4/subassets/basics-of-spi-serial-communications-presentation.pdf
  - https://community.nxp.com/t5/NXP-Tech-Blog/SPI%E3%83%90%E3%82%B9%E3%81%AE%E6%A6%82%E8%A6%81-%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%83%96%E3%83%AD%E3%82%B0/ba-p/2036964?profile.language=ja
