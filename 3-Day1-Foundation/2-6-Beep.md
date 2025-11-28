# PWMによるBeep音再生

PWMはDUTYを変えることでモータ制御等を行いますが、周波数を変えることで音階を再生することができます。
```
from machine import Pin
from machine import PWM
import time

PWM_OUT_PIN=16
freq = 300
pwm0 = PWM(Pin(PWM_OUT_PIN), freq=freq, duty_u16=int(0xffff/2))  # setup PWM
for freq in range(300,2000,10): 
    print(freq)
    pwm0.freq(freq)
    time.sleep(0.2)

# disable PWM
pwm0.deinit()
```
