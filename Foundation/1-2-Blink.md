# LED 点滅プログラム
Raspberry Pi Pico 2 Wのピン配置は以下となっています。GPIO番号をよくご確認ください。

LEDはGP16に接続します。LEDが点灯するかREPLで試しましょう
GP16を出力用に初期化するコードは以下
```
from machine import Pin
led = Pin(16, Pin.OUT)
```
点灯、消灯するプログラムは以下
```
led.on()
led.off()
```
