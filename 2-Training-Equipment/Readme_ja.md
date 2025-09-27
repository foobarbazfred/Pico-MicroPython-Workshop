# 研修用教材
## 使用教材
- マイコンはRaspberry Pi Pico 2Wを使用します
   - https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html
- プログラミング言語はMicroPythonです(CircuitPythonもありますが今回は使いません)
- マイコン、ブレッドボード、センサ類一式がキットとしてまとめられたFREENOVE社のStarter Kitを使用します。表示装置として、LCD、LED、NeoPixel、センサとして空気質センサ、距離センサ等が含まれます。
   - https://store.freenove.com/products/fnk0058
- キットを使う上でのマニュアル類は以下
   - https://docs.freenove.com/projects/fnk0058/en/latest/fnk0058/codes/Python.html
   - https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi_Pico/blob/master/Python/Python_Tutorial.pdf (PDF)
- キットに対応するドライバ類は以下
   - https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi_Pico/tree/master/Python

## 補助教材
何をどのように学んでもらうか、学習過程を考えた際、以下の教材を追加したい
1. 温湿度センサ；M5Stack用 温湿度CO2センサ（SCD41）(案)
   - 理由：IoTの基本として、空気質の計測が挙げられる。キット一式の中のセンサでもいいのだが、通信バスがI2Cでないのと、CO2を計測したいので、センサを追加したい
   - 課題：高い（１つ９千円）　ー＞　CO2必須としなければ、BME680等が利用可能 (ただ、あまり計測データの変化が発生しづらい)

## ファイル共有の仕組み
２日目は実際に手を動かして試作していただく。チーム構成としたい。この時、チームメンバでプログラムや設計書を共有できる仕組みが必要。大学様のネットワーク次第ですが、大学構内ネットワークの縛りがなければGoolgeDrive上等で共有するのも可能

## Document類 (参考資料)
- https://micropython-docs-ja.readthedocs.io/ja/latest/
- https://www.raspberrypi.com/documentation/microcontrollers/micropython.html
- https://github.com/micropython/micropython
- https://github.com/micropython/micropython-lib
- https://github.com/adafruit/circuitpython
- https://micropython-docs-ja.readthedocs.io/ja/latest/library/machine.I2S.html
- PDF形式ドキュメント
   - https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf
   - https://files.seeedstudio.com/wiki/Grove_Shield_for_Pi_Pico_V1.0/Begiinner%27s-Guide-for-Raspberry-Pi-Pico.pdf
   - https://docs.freenove.com/projects/fnk0058/en/latest/fnk0058/codes/Python.html
   - https://github.com/raspberrypipress/released-pdfs/blob/main/get-started-with-micropython-raspberry-pi-pico.pdf
 - sample source
   - https://github.com/miketeachman/micropython-i2s-examples/blob/master/examples/play_wav_from_sdcard_blocking.py

