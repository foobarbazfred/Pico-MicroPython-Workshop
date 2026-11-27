# SPIによるデバイスとの接続

SPI（Serial Peripheral Interface）バスは周辺機器との接続で使われます。
- SPIバスはモトローラによって開発され、現在はNXPが仕様を管理
- SPIバスは、SCLK(クロック)、MOSI（Master Out Slave In）(送信)、MISO（Master In Slave Out）(受信)、CS(Chip Select)の４線で接続します
- SCLK,MOSI,CSはマスター（マイコン）側が制御します
- I2Cと比べて高速通信が可能です。SPIでは設計上、数十MHzの速度でデータを送受信することが可能です。
- SPIは複数デバイスを接続することができます。通信したいデバイスのCS(Chip Select)をLにすることで、通信先デバイスを指定します

SPIバスの仕様上、マスタ・スレーブ間のデータの送受信(物理層)は規定されていますが、データをどう扱うのか（論理層）については規定されていません。例えば、センサがレジスタを持つ場合、センサのレジスタに値を書き込むのか、センサのレジスタから値を読み込むのか、SPIバスの仕様には定義されていません。このような使い方はデバイス各社がデータの扱いを独自に決めて運用しています。どのように制御するかはデバイスの仕様書を参照して判断します。なお、有名なセンサ類はMicroPython版ドライバが有志によって開発、公開されています。自作する前に、使いたいセンサのドライバが公開されていないか、検索することをお勧めします。

SPIバスによる制御例として、CMOSカメラ、SDカード、角速度センサ、距離センサ等があります。本研修では時間の都合上、SDカードの接続演習は行いませんが、接続方法について、テキストに記載しています。またキットには、RFIDカードの読み書きができるRFID-RC522が含まれています。このRFID-RC522はコントローラとしてMFRC522が使われており、SPIで制御できます。

### 参考資料
https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#hardware-spi-bus<br>
https://github.com/vtt-info/MicroPython_MFRC522/tree/main
https://docs.freenove.com/projects/fnk0058/en/latest/fnk0058/codes/Python/28_RFID.html
