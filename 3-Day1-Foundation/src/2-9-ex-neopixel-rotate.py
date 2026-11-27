#
# file: 2-9-ex-neopixel-rotate.py
# 機能：8個のNeoPixelの点灯位置を順番に切り替え、光が回転するように見せるサンプル
#
import time
from machine import Pin
from neopixel2 import myNeopixel
NUM_LEDS = 8
PIN_NO = 16
np = myNeopixel(NUM_LEDS, PIN_NO)

led_r = 10
led_g = 100
led_b = 100

prev_pos = None
while True:
   for pos in range(NUM_LEDS):
       if prev_pos is not None:
           np.set_pixel(prev_pos, 0,0,0)
           np.show()
       np.set_pixel(pos, led_r, led_g, led_b)
       np.show()
       prev_pos = pos
       time.sleep(0.02)
