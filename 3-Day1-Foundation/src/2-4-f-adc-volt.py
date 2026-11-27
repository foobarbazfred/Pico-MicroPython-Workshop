#
# file: 2-4-f-adc-volt.py
# 機能：ボリュームで設定された電圧をAD変換し、値と推定電圧を表示するサンプル
#
from machine import ADC, Pin
import time
MAX_VALUE = 0xffff
MAX_VOLT = 3.3
adc = ADC(Pin(26))     # create ADC object on ADC pin

while True:
    value = adc.read_u16()
    estim_vol = MAX_VOLT * value / MAX_VALUE
    print(value, hex(value), estim_vol, 'V')
    time.sleep(0.5)
#
#
