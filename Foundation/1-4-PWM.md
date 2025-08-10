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
```
from machine import Pin
from machine import ADC
from machine import PWM

import time
MAX_VALUE = 0xffff
MAX_VOLT = 3.3
adc = ADC(Pin(26))     # create ADC object on ADC pin

pwm0 = PWM(Pin(16), freq=2000, duty_u16=0)  # setup PWM

while True:
    value = adc.read_u16()
    pwm0.duty_u16(value)
    estim_vol = MAX_VOLT * value / MAX_VALUE
    print(value, hex(value), estim_vol, 'V')

#
#
```

自動的に点滅するプログラムは以下(sinを使っています)
```
from machine import Pin
from machine import PWM
import math

import time
MAX_VALUE = 0x4000

pwm0 = PWM(Pin(16), freq=2000, duty_u16=0)  # setup PWM
while True:
    for i in range(0, 30 , 1):  # 30 means math.pi * 10
        value = int(MAX_VALUE * math.sin(i/10))    # i/10 means math.pi * 10 -> math.py
        pwm0.duty_u16(value)
        time.sleep(0.5)
```

参考WebPage<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#pwm-pulse-width-modulation
