# PWMによるBeep音再生

PWMはDUTYを変えることでモータ制御等を行いますが、周波数を変えることで音階を再生することができます。
```
from machine import Pin
from machine import PWM
import time

# setup PWM output
PWM_OUT_PIN=16
freq = 300
pwm0 = PWM(Pin(PWM_OUT_PIN), freq=freq, duty_u16=int(0xffff/2)) 

# loop 
for freq in range(300,2000,10): 
    print('freq:', freq)
    pwm0.freq(freq)
    time.sleep(0.1)

# finally; disable PWM
pwm0.deinit()
```
研修では、株式会社村田製作所の圧電スピーカー(圧電サウンダー)PKM22EPPH4001-B0を使用しています。この圧電スピーカは極性がなく、端子に再生させたい周波数の信号を与えることで、スピーカで音が再生されます。4KHzが最も音圧が高く、最高は10KHzまで再生できるようです。<br>
部品説明ページ<br>
https://pim.murata.com/ja-jp/pim/details/?partNum=PKM22EPPH4001-B0
