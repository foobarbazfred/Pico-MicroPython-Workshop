#
# file: 3-8-f-distance-sensor.py
# 機能：超音波距離センサ(HC-SR04)で対象物までの距離とパルス幅を計測し、シリアルコンソールに表示するサンプル
#
import time
from machine import Pin
from hc_sr04 import HC_SR04

# setup
trig = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
hc_sr04 = HC_SR04(trig,echo)

# loop
while True:
  distance, pulse_width = hc_sr04.measure()   # 
  #print(pulse_width)

  report = f"dist: {distance:0.2f} cm\npulse: {pulse_width} usec"
  print("-------------------")
  print(report)
  time.sleep(1)

# end of file
