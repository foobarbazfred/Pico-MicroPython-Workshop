# センサ等とシリアルバスで接続する

センサや表示装置はシリアルI/Fで接続する場合が多いです。主なシリアルI/Fとして以下が挙げられます
1. UART
2. I2C
3. SPI

今回の演習ではI2Cを使ってセンサ、表示装置と接続します。
I2Cは＃＃＃によって規定されたバス仕様であり、＃＃＃、＃＃＃、＃＃＃が特徴です。I2Cデバイスは複数のデバイスが接続できるように設計されており、基本的にデバイスはプルアップ抵抗が付けられていません。このため、I2Cバス用にプルアップを付ける必要があります。
I2Cは双方向バスであり、バスを制御するマスター側とマスターから提示された信号に応じて応答するスレーブ側に分かれます。＃＃＃から＃＃＃を出します。各デバイスはアドレスを持っており、通信する際は通信したいデバイスのアドレスを指定してデータを送受信します。

## I2Cを利用するには

I2Cバスを利用する上で、信号を作り出すハードウエアの観点と、I2Cバスを利用してデータを送受信するソフトウエアの観点があります。I2Cバスの信号を作り出すハードウエアは、I2C用周辺IOを使うハードウエア実装と、ソフトウエアによりI2C信号を作り出すソフトウエア実装があります。

#### I2Cで接続されたデバイスを利用する際のソフトウエア、ハードウエア階層
```
|Application｜                  |Device｜
|Device Driver｜                |Device Driver｜
|I2C Driver|                    |I2C Driver|
|I2C ＨＷ｜ ==================　|I2C HW|

```
MicroPythonではH実装、S実装のいずれも利用可能であり、I2Cの初期化時に設定します。以下I2Cの初期化例を示します。

### Hardware I2Cの利用
H実装のI2CバスはI2C0, I2C1の2チャンネル利用可能です。HW実装の場合、使えるピンは制限があり、ピン配置図から選んでください。
何も指定しないと、I2C0の場合は、Pin4, Pin5、I2C1の場合はPin2, Pin3が割り当てられます。
```
# initialize I2C
from machine import Pin, I2C
i2c_0 = I2C(0)   # H/W I2C ch_0  scl=Pin(5), sda=Pin(4), freq=400_000
i2c_1 = I2C(1)   # H/W I2C ch_1  scl=Pin(3), sda=Pin(2), freq=400_000
```


### software I2Cの利用
```
# initialize I2C
from machine import Pin, SoftI2C
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=100_000)
```

### I2C I/Fで接続されたデバイスとの通信
デバイスの接続確認
```
i2c.scan()
```
デバイスからのデータ受信
```
ADDR = 0x3F        #  接続先デバイスのアドレス（例）
data = i2c.readfrom(ADDR, nbytes)
```
デバイスへのデータ送信
```
ADDR = 0x3F        #  接続先デバイスのアドレス（例）
data = bytes(0x00,0x01,0x02)
i2c.writeto(ADDR, data)
```

## 参考情報
- RP2 用クイックリファレンス
  - https://micropython-docs-ja.readthedocs.io/ja/latest/rp2/quickref.html#hardware-i2c-bus
- クラスI2C
  - https://micropython-docs-ja.readthedocs.io/ja/latest/library/machine.I2C.html#class-i2c-a-two-wire-serial-protocol
- I2Cバス仕様書 (I2Cバス仕様およびユーザーマニュアル)
  - chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.nxp.com/docs/ja/user-guide/UM10204.pdf
