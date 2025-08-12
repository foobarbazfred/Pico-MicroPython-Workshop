# アナログ値の取り扱い

GP26のADC0を使用します。ADCの初期化は以下です
```
from machine import ADC, Pin
adc = ADC(Pin(26))     # create ADC object on ADC pin
```
値を読み取ってみましょう
```
adc.read_u16()         # read value, 0-65535 across voltage range 0.0v - 3.3v
```
GP26にかかっている電圧が0Vの場合、adc.read_u16()の値は0になります。一方、電圧が3.3Vの場合、65535(0xffff)となります。
ADCを使うことにより0Vから3.3Vの間で変化する電圧を数値化することができます。
アナログ値を取得して一定周期でprintするプログラムとしてまとめると以下です
```
from machine import ADC, Pin
import time
adc = ADC(Pin(26))     # create ADC object on ADC pin

while True:
    value = adc.read_u16()
    print(value, hex(value))
    time.sleep(0.5)
```
推定電圧も含めたサンプルコードは以下
```
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
```
