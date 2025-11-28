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
本研修では、株式会社村田製作所の圧電スピーカー(圧電サウンダー)PKM22EPPH4001-B0を使用しています。この圧電スピーカは極性がなく、端子に再生させたい周波数の信号を与えることで、スピーカから音が再生されます。4KHzが最も音圧が高く、最高10KHzまで再生できるようです。<br>
部品説明ページ<br>
https://pim.murata.com/ja-jp/pim/details/?partNum=PKM22EPPH4001-B0

音と周波数の関係は決まっています。例えば以下のサイトは、一覧表を掲示されています。<br>
https://khufrudamonotes.com/frequencies-for-equal-tempered-scale<br>
https://www.asahi-net.or.jp/~hb9t-ktd/music/Japan/Research/DTM/freq_map.html

簡単に、中央のド付近(4オクターブ)の音階と周波数を抜粋します

| 音名 | 記号 |  周波数(Hz) |
|--|--|--|
| ド | C4 | 262 |
| レ | D4 | 294 |
| ミ | E4 | 330 |
| ファ | F4 | 349 |
| ソ | G4 | 392 |
| ラ | A4 | 440 |
| シ | B4 | 494 |
| ド | C5 | 523 |

