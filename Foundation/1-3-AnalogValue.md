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
GP26にかかっている電圧が0Vの場合、adc.read_u16()の値は0になります。一方、電圧が3.3Vの場合、64435(0xffff)となります。
ADCを使うことにより0Vから3.3Vの間で変化する電圧を数値化することができます。
