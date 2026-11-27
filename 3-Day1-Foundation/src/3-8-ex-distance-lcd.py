#
# file: 3-8-ex-distance-lcd.py
# 機能：超音波距離センサ(HC-SR04)で計測した距離とパルス幅をI2C接続のLCDディスプレイに表示する演習サンプル
#
import time
from machine import Pin
from hc_sr04 import HC_SR04

# setup
LCD_AVAILABLE = True
trig = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
hc_sr04 = HC_SR04(trig,echo)

if LCD_AVAILABLE:
   from st7032 import ST7032LCD
   from machine import I2C
   i2c_1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=400_000)
   lcd =  ST7032LCD(i2c_1)

# loop
while True:
  distance, pulse_width = hc_sr04.measure()   # 
  #print(pulse_width)

  report = f"dist: {distance:0.2f} cm\npulse: {pulse_width} usec"
  print("-------------------")
  print(report)
  if LCD_AVAILABLE:
     lcd.print(report, cls=True)
  time.sleep(1)

# end of file
