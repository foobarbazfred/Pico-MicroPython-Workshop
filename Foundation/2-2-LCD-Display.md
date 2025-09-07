# LCD Displayの利用

LCD Displayは16x2が表示可能、コントローラはPCF8574T (PCF8574AT)が使われています。I2Cで接続され、デバイスアドレスは0x27です。
マイコンとの接続は、5V,GNDに加え、I2Cのクロック、データバスを接続します。

先ほど説明に従い、HW I2Cを使いI2C_0でデフォルトで接続してみます。
```
from machine import Pin, I2C
i2c_0 = I2C(0)
```
正しく接続できているか、scan関数で確認します
```
i2c_0.scan()
```
以下が実行結果です
```
>>> from machine import Pin, I2C
>>> i2c_0 = I2C(0)
>>> i2c_0.scan()
[39]
>>> hex(i2c_0.scan()[0])
'0x27'
```
IOとしてどのPinを使用するか指定せず、デフォルトにまかせていました。設定内容を確認することもできます
```
>>> i2c_0
I2C(0, freq=400000, scl=5, sda=4, timeout=50000)
```
上記結果より、SCK:GPIO5、SDA:PGIO4, I2Cバスのクロック50KHz (50_000)であることが分かります。
LCDに文字を表示するには、RAM領域にASCIIコードを書き込む必要があります。プログラムですべて実装するのは大変なので、LCD用ドライバを活用して、プログラム量を減らせられます。
LCD用ドライバとして＃＃＃、＃＃＃、＃＃＃がありますが、今回使っているキットのメーカが提供するLCDドライバを活用します。




The serial-to-parallel IC chip used in this module is PCF8574T (PCF8574AT), and its default I2C address is 0x27(0x3F).
