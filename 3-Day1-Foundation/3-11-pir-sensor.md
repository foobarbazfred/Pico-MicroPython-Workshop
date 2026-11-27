# 人感センサ(焦電型赤外線センサ)

人感センサを使うことで、人が近づいたことを検知することができます。例えば、以下は焦電型赤外線センサー PaPIRs(VZ) 5m EKMC1601112です。

出力はデジタル１本のL/Hであり、人が近づいたら1(3.3V)になります。マイコン側からの設定等は不要です。

PaPIRsのデジタル出力はFETドレイン出力（ハイサイドのオープンドレイン）です。未検知時の出力レベルをLowに確定させるためにセンサーの外側にプルダウン抵抗が必要です。出力最大電流が100uAなので、47KΩから100KΩの外付け抵抗でLowにPull Downします。本来の回路図と簡単なテストプログラムは以下です
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
        print('Detected')
    else:
        print('Not detected')
    time.sleep(1)

```
本来は上記回路とテストプログラムで動作しますが(RP2040 (Raspberry Pi Picoで確認))、RP2350-E9 erratumで示されるように、RP2350のGPIOに回路上の問題があり、Pull Down機能が正しく動作しません。回避手段としては、センサとマイコンの間にMOSFETやトランジスタを介して、追加されたデバイスでプルダウンとL/Hの変化を受けてGPIOに信号を送る方法が考えられます。


### ご参考
* [RP2350 Datasheet(Errata - RP2350-E9) (Appendix D: D.5. GPIO D.5.1. RP2350-E9)](https://pip.raspberrypi.com/documents/RP-008373-DS-rp2350-datasheet.pdf)　
* [PaPIRs(VZ) 5m EKMC1601112仕様書](https://industrial.panasonic.com/cdbs/www-data/pdf/EWA0000/ast-ind-247460.pdf)
* [焦電型赤外線人感センサ Q&A集2025](https://industrial.panasonic.com/cdbs/www-data/pdf/EWA0000/ast-ind-250616.pdf)

