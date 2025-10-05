# I2SによるDA変換装置との接続

非圧縮の音データを送信するための仕様として、I2S (I squre Sound)があります。これは以下のような信号の仕様となっており、下記３つの信号で音データが送信されます。
- 16bit/24bit長の音データ
- L/Rのいずれであるかを示すLRCLK
- 1bitの音信号を示すCLK

サンプリングレートは最低で、8KHz、最高で#KHzとなっています。このレートはADコンバータの仕様により決まります。

<img src="assets/Schematics_i2s_spaker.png" width=400>
