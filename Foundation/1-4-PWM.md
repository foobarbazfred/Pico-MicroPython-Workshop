# PWMによる疑似アナログ出力

RP2350にはDA変換が搭載されていませんので、直接アナログ出力することができません。代替手段として、PWMを用いて、0、1(3.3V)以外の値を表現することができます。
LEDを点滅、点灯以外に、PWMを使うことで暗く光らせることができます。

PWMを使ってLEDを中間的な明るさで点灯させるプログラム
```
from machine import Pin
from machine import PWM

pwm0 = PWM(Pin(16), freq=2000, duty_u16=int(0xffff/4))
pwm0.duty_u16(1000)
```

先ほどのボリュームと連動して明るさを調整するプログラムは以下



参考WebPage<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#pwm-pulse-width-modulation
