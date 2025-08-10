# 1-1  シンプルなLED点滅ぷろぐらむ

配線も不要でボード上のLEDを点滅させるプログラムは以下
```
from machine import Pin
import tiem
led = Pin('LED', Pin.OUT)
while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
```
