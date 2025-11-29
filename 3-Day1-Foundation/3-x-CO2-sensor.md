# CO2センサの接続

- Senserion SCD41
- 温度、湿度、CO2濃度

デバイス接続テスト
```
>>> hex(i2c.scan()[0])
'0x62'
```

MPU-6050用のドライバが提供されていますのでこれを使用します。
多くのドライバは呼び出し側でI2Cバスを初期化して引数として渡しますが、mpu6050用ドライバ(mpu6050)では
ドライバ側でI2Cを初期化します。引数としてはI2CのチャンネルとGPIO番号を指定します。

```
 self.i2c = I2C(id=bus, scl=Pin(sclpin), sda=Pin(sdapin), freq=400000)
```
```


```

```

```
## 組み合わせ例
1. モーションセンサとLCDキャラクタディスプレイ
   - モーションセンサを傾けると、傾きに応じてディスプレイの表示が左右に揺れる
2. モーションセンサとカラーLED
   - モーションセンサの回転に合わせてカラーLEDの点灯位置が回る
     

### 参考資料
- https://github.com/Freenove/Freenove_Ultimate_Starter_Kit_for_Raspberry_Pi_Pico/blob/master/Python/Python_Libraries/mpu6050.py
- https://product.tdk.com/ja/search/sensor/mortion-inertial/imu/info?part_no=MPU-6050
- https://invensense.tdk.com/wp-content/uploads/2015/02/MPU-6000-Register-Map1.pdf


Sensirion Drvier
https://github.com/Sensirion/python-i2c-scd/tree/master/sensirion_i2c_scd/scd4x