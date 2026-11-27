#
# file: 2-5-f-led-blink-pwm.py
# 機能：PWMの最低周波数(8Hz @125MHz)とデューティ比50%でLEDを点滅させるサンプル
#
import machine
from machine import Pin
from machine import PWM
PWM_OUTPUT_PIN=16

# setup
machine.freq(125_000_000)
# set lowest PWM FREQ 8Hz
pwm0 = PWM(Pin(PWM_OUTPUT_PIN), freq=8, duty_u16=int(0xffff/2))
#
#
