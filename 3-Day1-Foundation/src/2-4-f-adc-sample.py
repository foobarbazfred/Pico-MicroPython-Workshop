#
# file: 2-4-f-adc-sample.py
# 機能：ボリュームで設定された電圧をAD変換、変換結果を表示するサンプル
#
from machine import ADC, Pin
import time
adc = ADC(Pin(26))     # create ADC object on ADC pin

while True:
    value = adc.read_u16()
    print(value, hex(value))
    time.sleep(0.5)
