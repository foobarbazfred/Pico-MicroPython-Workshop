# I2SによるDAコンバータとの接続

非圧縮の音データを送信するための仕様として、I2S (Inter-IC Sound)があります。これはNXPにより策定された仕様であり、以下のような信号の仕様となっており、下記３つの信号で音データが送信されます。
- 16bit/24bit長の音データ(SD)
- L/Rのいずれであるかを示すLRCLK
- 1bitの音信号を示すCLK

DAC（Digital to Analog Converter）や ADC（Analog to Digital Converter）との接続で使われます。

サンプリングレートは最低で、8KHz、最高で#KHzとなっています。どのようなサンプリングレートを指定できるかはDACの仕様により決まります。

<img src="assets/Schematics_i2s_spaker.png" width=400>

https://github.com/foobarbazfred/Pico-MicroPython-Workshop/blob/main/3-Day1-Foundation/src/lib/I2S_sample4.py
