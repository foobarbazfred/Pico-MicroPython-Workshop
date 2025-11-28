# PWMによる疑似アナログ出力

RP2350にはDA変換が搭載されていませんので、直接アナログ出力することができません。代替手段として、PWMを用いて、0、1(3.3V)以外の値（中間値）を表現することができます。もう少し詳しく説明すると、出力するパルス幅の比率を使って平均電力を変化させます(PWM : Pulse Width Modulation)。PWMで疑似的に表現された0/1のパルスをローパスフィルタ(LPF)（積分回路）に通すと、アナログ値が取り出せます。この講習では、LPFは使わず、そのままデバイスに投入します。

LEDを点滅、点灯以外に、PWMを使うことで暗く光らせることができます。
PWMを使ってPWMの設定可能な最も低い周波数で点滅させるプログラム
```
from machine import Pin
from machine import PWM
PWM_OUTPUT_PIN=28
pwm6 = PWM(Pin(PWM_OUTPUT_PIN), freq=8, duty_u16=int(0xffff/2))
# change duty
pwm6.duty_u16(int(0xffff/16))
```

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

自動的に点滅するプログラムは以下(sinを使っています)<br>
Pythonのrange()は小数点を使えないので、0 -> 3.14の変化を作り出すのに、0 -> 314 で代用しています
```
from machine import Pin
from machine import PWM
import math

import time
MAX_VALUE = 0x4000

pwm0 = PWM(Pin(16), freq=2000, duty_u16=0)  # setup PWM
while True:
    for i in range(0, 314 , 1):  # 314 means math.pi * 100
        value = int(MAX_VALUE * math.sin(i/100))    # i/100 means math.pi * 100 -> math.py
        pwm0.duty_u16(value)
        time.sleep(0.01)
```

参考WebPage<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#pwm-pulse-width-modulation
