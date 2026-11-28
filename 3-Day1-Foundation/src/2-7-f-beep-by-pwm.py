#
# file: 2-7-f-beep-by-pwm.py
# 機能：PWMの周波数を300Hzから2000Hzまで変化させ、圧電サウンダから音を鳴らすサンプル
#
from machine import Pin
from machine import PWM
import time

# setup PWM output
PWM_OUT_PIN=16
freq = 300
pwm0 = PWM(Pin(PWM_OUT_PIN), freq=freq, duty_u16=int(0xffff/2)) 

# loop 
for freq in range(300, 2000, 10): 
    print('freq:', freq)
    pwm0.freq(freq)
    time.sleep(0.1)

# finally; disable PWM
pwm0.deinit()
