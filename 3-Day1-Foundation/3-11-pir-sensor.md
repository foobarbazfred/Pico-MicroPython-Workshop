# 人感センサ(焦電型赤外線センサ)

人感センサを使うことで、人が近づいたことを検知することができます。例えば、以下は焦電型赤外線センサー PaPIRs(VZ) 5m EKMC1601112です。

出力はデジタル１本のL/Hであり、人が近づいたら1(3.3V)になります。マイコン側からの設定等は不要です。
回路図は以下です。人を検知しない時、内蔵されている＃＃＃がオープンになっていますので、抵抗でプルダウンしてLに落とす必要があります。RP2350のGPIOにはPull Up機能、Pull Down機能がありますが、erratum RP2350-E9で示されるように、Pull Down機能が正しく動作しません。今回は、10KΩの外付け抵抗で0VにPull Downしています。

簡単なテストプログラムは以下です
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
wnile True:
    if(sensor_pin.value() == 1):
        print('detect human')
    else:
        print('detect none')
    time.sleep(1)

```




#### ご参考
erratum RP2350-E9「Bank 0 pull-down resistors latching behavior」
PaPIRs(VZ) 5m EKMC1601112仕様書<br>
https://industrial.panasonic.com/cdbs/www-data/pdf/EWA0000/ast-ind-247460.pdf
