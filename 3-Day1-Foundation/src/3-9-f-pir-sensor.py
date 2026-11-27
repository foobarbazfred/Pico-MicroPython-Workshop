#
# file: 3-9-f-pir-sensor.py
# 機能：焦電型赤外線人感センサ(PaPIRs)の出力を読み取り、人の検知状態を定期的に表示するサンプル
#

import time
from machine import Pin
PIR_SENSOR_PIN = 0

# setup
sensor_pin = Pin(PIR_SENSOR_PIN, Pin.IN)

# loop
while True:
    if sensor_pin.value() == 1:
        print('Detected')
    else:
        print('Not detected')
    time.sleep(1)

