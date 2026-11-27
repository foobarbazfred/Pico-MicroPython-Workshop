#
# file:2-2-f-blink.py
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

