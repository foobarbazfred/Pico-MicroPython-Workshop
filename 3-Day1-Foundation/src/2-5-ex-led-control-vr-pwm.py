#
# file: 2-5-ex-led-control-vr-pwm.py
# 機能：ボリューム（可変抵抗）のAD変換値に連動してPWMのデューティ比を変え、LEDの明るさを調整するサンプル
#
from machine import Pin
from machine import ADC
from machine import PWM

import time
MAX_VALUE = 0xffff
MAX_VOLT = 3.3

VR_PIN=26
LED_PIN=16

# setup
adc = ADC(Pin(VR_PIN))     # create ADC object on ADC pin
pwm0 = PWM(Pin(LED_PIN), freq=2000, duty_u16=0)  # setup PWM

# loop
while True:
    value = adc.read_u16()
    pwm0.duty_u16(value)
    estim_vol = MAX_VOLT * value / MAX_VALUE
    print(value, hex(value), estim_vol, 'V')

#
#
