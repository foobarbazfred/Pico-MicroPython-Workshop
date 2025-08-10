# PWMによるBeep音再生

PWMはDUTYを変えることでモータ制御等を行いますが、周波数を変えることで音階を再生することができます。
```
from machine import Pin
from machine import PWM
import time

freq = 100
pwm0 = PWM(Pin(16), freq=freq, duty_u16=int(0xffff/2))  # setup PWM
for freq in range(400,2000,10): 
    print(freq)
    pwm0.freq(freq)
    time.sleep(0.2)
```
