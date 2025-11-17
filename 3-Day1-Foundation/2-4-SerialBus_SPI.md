# SPIによるデバイスとの接続

SPI（Serial Peripheral Interface）バスは周辺機器との接続で使われます。
- SPIバスはモトローラによって開発され、現在はNXPが仕様を管理
- SPIバスは、SCLK(クロック)、MOSI（Master Out Slave In）(送信)、MISO（Master In Slave Out）(受信)、CS(Chip Select)の４線で接続します
- SCLK,MOSIはマイコン側が制御します
- I2Cと比べて高速通信が可能になる点が特徴です。SPIでは設計上、数十MHzの速度でデータを送受信することが可能です。
- SPIは複数デバイスを接続することができます。通信したいデバイスのCS(Chip Select)をLにすることで、通信先デバイスを指定します

SPIバスによる制御例としてRFIDの受信を取り上げます。キットには、RFID-RC522が含まれています。このRFID-RS522は、＃＃＃、＃＃であり、I2C, SPI両方のバス接続に対応しています。
SPIの理解のため、SPIで接続します。




https://github.com/vtt-info/MicroPython_MFRC522/tree/main
