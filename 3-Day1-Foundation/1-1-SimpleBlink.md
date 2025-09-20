# 1-1  シンプルなLED点滅プログラム

配線も不要でボード上のLEDを点滅させるプログラムは以下
```
from machine import Pin
import time

led = Pin('LED', Pin.OUT)
while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
```

ボード上のBOOTSELボタンに連動してLEDが点灯するプログラムは以下
```
from machine import Pin
from rp2 import bootsel_button

led = Pin('LED', Pin.OUT)
while True:
    if bootsel_button() == 1:
        led.on()
    else:
        led.off()
```

上記いずれも配線済みのLEDやボタンを使ってテストしました。次は配線してLEDを点滅させましょう
