#
# file:2-2-f-blink.py
# 概要: 押しボタンスイッチの入力に応じてLEDを点灯/消灯する基本プログラム
#
from machine import Pin

# setup
led = Pin(16, Pin.OUT)
sw = Pin(15, Pin.IN, Pin.PULL_UP)

# loop
while True:
    print(sw.value())
    if sw.value() == 0:
        led.on()
    else:
        led.off()

