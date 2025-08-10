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
