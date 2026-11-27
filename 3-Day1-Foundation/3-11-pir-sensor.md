# 人感センサ(焦電型赤外線センサ)

人感センサを使うことで、人が近づいたことを検知することができます。例えば、以下は焦電型赤外線センサー PaPIRs(VZ) 5m EKMC1601112です。

出力はデジタル１本のL/Hであり、人が近づいたら1(3.3V)になります。マイコン側からの設定等は不要です。

PaPIRsのデジタル出力はFETドレイン出力（ハイサイドのオープンドレイン）です。未検知時の出力レベルをLowに確定させるためにセンサーの外側にプルダウン抵抗が必要です。47KΩから100KΩの外付け抵抗でLowにPull Downします。本来の回路図と簡単なテストプログラムは以下です
```
#
# test program for Pyroelectric Infrared Sensor
#
import time
from machine import Pin
PIR_SENSOR_PIN = 0

# setup
sensor_pin = Pin(PIR_SENSOR_PIN, Pin.IN)

# loop
while True:
    if(sensor_pin.value() == 1):
        print('detect human')
    else:
        print('not detected')
    time.sleep(1)

```
本来は上記回路とテストプログラムで動作しますが、RP2350-E9 erratumで示されるように、RP2350のGPIOに回路上の問題があり、Pull Down機能が正しく動作しません。代替手段としてAD変換して電圧を検知します。



#### ご参考
RP2350-E9 erratum: input pin can become latched at about ~2V
PaPIRs(VZ) 5m EKMC1601112仕様書<br>
https://industrial.panasonic.com/cdbs/www-data/pdf/EWA0000/ast-ind-247460.pdf<br>
焦電型赤外線人感センサ Q&A集2025<br>
https://industrial.panasonic.com/cdbs/www-data/pdf/EWA0000/ast-ind-250616.pdf<br>
