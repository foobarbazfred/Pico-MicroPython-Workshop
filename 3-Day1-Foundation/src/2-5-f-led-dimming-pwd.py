#
# file: 2-5-f-led-dimming-pwd.py
# 機能：PWMのデューティ比を切り替えてLEDの明るさ（100%と25%）を変化させるサンプル
#
from machine import Pin
from machine import PWM
import time
LED_PIN=16

# setup
pwm0 = PWM(Pin(LED_PIN), freq=2_000, duty_u16=int(0xffff/4))

# loop
while True:
    pwm0.duty_u16(0xFFFF)
    time.sleep(1)
    pwm0.duty_u16(int(0xffff/4))
    time.sleep(1)
#
#
