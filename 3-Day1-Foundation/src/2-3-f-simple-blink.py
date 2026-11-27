#
# file:2-3-f-simple-blink.py
# 概要: ボード上の押しボタンスイッチの入力に応じてボード上のLEDを点灯/消灯するプログラム
#
from machine import Pin
from rp2 import bootsel_button

# setup for LED Pin
led = Pin('LED', Pin.OUT)

# loop; LED on if button is pressed
while True:
    if bootsel_button() == 1:
        led.on()
    else:
        led.off()
#
#
