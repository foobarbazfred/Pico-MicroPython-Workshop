#
# file: 2-5-ex-led-blink-pwm-sin.py
# 機能：sin関数を使ってPWMのデューティ比を連続変化させ、LEDを滑らかに明滅させるサンプル
#
from machine import Pin
from machine import PWM
import math

import time
MAX_VALUE = 0xFFFF
LED_PIN=16
# setup
pwm0 = PWM(Pin(16), freq=2000, duty_u16=0)  # setup PWM

# loop
while True:
    for i in range(0, 314 , 1):  # 314 means math.pi * 100
        value = int(MAX_VALUE * math.sin(i/100))    # i/100 means math.pi * 100 -> math.py
        pwm0.duty_u16(value)
        time.sleep(0.01)
#
#
