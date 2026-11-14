# マイコンとセンサを接続するシリアルインタフェース(I/F)

センサや表示装置との接続は、一般にUART・I2C・SPIなどのシリアルインタフェースが使われます。本章では代表的な3種類のインタフェースを整理します。

|シリアルインタフェース仕様名|接続信号(*)|特徴|
|--|--|--|
|UART<br>(Universal Asynchronous Receiver/Transmitter)|送信信号(TX)、受信信号(RX)|クロックが不要<br>一対一通信<br>全二重通信|
|I2C<br>(Inter-Integrated Circuit)|クロック(SCL)、送受信信号(SDA)|クロック必要<br>１本の信号線で送受信を切り替える<br>SCL/SDAを共有することで複数のターゲットが接続可能<br>半二重通信|
|SPI<br>(Serial Peripheral Interface)|クロック(SCLK)、送信信号(MOSI)、受信信号(MISO)、CS|クロック必要<br>送信用信号と、受信用信号が分かれる<br>SCLK/MOSI/MISOを共有することで複数のターゲットが接続可能<br>高速通信可能<br>全二重通信|

*:接続信号のうち、電源、GNDは除いています

ご参考：その他のシリアルI/F
- 1-Wire (クロックが不要で、双方向データ信号１本、ただし低速)
- QSPI (SPIをベースとしつつ、データ信号が４本)
- I2S (音声データ専用のシリアルインタフェース)


### 周辺デバイスとシリアルI/F
マイコンと周辺デバイスとの接続には、製品によってさまざまなシリアルI/Fが使われます。代表的な例を示します。同じ種類のデバイスでも製品ごとに異なる場合があります。
- UART
  - 低解像度CMOSカメラ
  - 音声合成デバイス
  - GPS
- I2C
  - 温度センサ、気圧センサ等各種センサ
  - CMOSカメラ(センサ部制御)
  - キャラクタ液晶ディスプレイ
- SPI
  - 各種センサ(DOFセンサ等(6軸/9軸IMU等))
  - CMOSカメラ(フレームバッファ付き)(データ転送)
  - グラフィック液晶ディスプレイ     

演習では主にI2Cを使ってセンサ、液晶ディスプレイと接続します。

## 参考情報
- MicroPython Documents; RP2 用クイックリファレンス
  - https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#uart-serial-bus 
  - https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#hardware-spi-bus
  - https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#hardware-i2c-bus
- クラスI2C
  - https://micropython-docs-ja.readthedocs.io/ja/latest/library/machine.I2C.html#class-i2c-a-two-wire-serial-protocol
- I2Cバス仕様書 (I2Cバス仕様およびユーザーマニュアル)(NXP)
  - https://www.nxp.com/docs/ja/user-guide/UM10204.pdf
- SPI解説文
  - https://www.ti.com/content/dam/videos/external-videos/en-us/6/3816841626001/6163521589001.mp4/subassets/basics-of-spi-serial-communications-presentation.pdf
  - https://community.nxp.com/t5/NXP-Tech-Blog/SPI%E3%83%90%E3%82%B9%E3%81%AE%E6%A6%82%E8%A6%81-%E6%97%A5%E6%9C%AC%E8%AA%9E%E3%83%96%E3%83%AD%E3%82%B0/ba-p/2036964?profile.language=ja
  - https://web.pa.msu.edu/people/edmunds/Disco_Kraken/SPI_Documents/motorola_freescale_nxp_spi_manual_2000.pdf
