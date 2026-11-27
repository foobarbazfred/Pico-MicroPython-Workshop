#
# file: 3-7-ex-motion-lcd.py
# 機能：6軸モーションセンサ(MPU6050)から取得した加速度の値をI2C接続のLCDディスプレイに表示するサンプル
#
import time
from machine import Pin
from machine import I2C
from I2C_LCD import I2CLcd
from mpu6050 import MPU6050

LCD_ADDR = 0x27
i2c_1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=400_000)
lcd = I2CLcd(i2c_1, LCD_ADDR, 2, 16)

G = 9.8
mpu = MPU6050(0, 5, 4)     #bus(0), SCL(GP5), SDA(GP4)
mpu.MPU_Init() #initialize the MPU6050
time.sleep(1)  #waiting for MPU6050 to work steadily

while True:
    accel = mpu.MPU_Get_Accelerometer() #gain the values of Acceleration
    gyro = mpu.MPU_Get_Gyroscope()      #gain the values of Gyroscope
    print('----------------------------------------')
    print('raw accel:', accel)
    print('raw gyro:', gyro)
    print('----------------------------------------')
    print('accel:', (accel[0]/16384, accel[1]/16384, accel[2]/16384))
    print('gyro:', (gyro[0]/131, gyro[1]/131, gyro[2]/131))
    print('----------------------------------------')
    lcd.clear()
    lcd.putstr(f'{accel[0]/16384:.1f},{accel[1]/16384:.1f},{accel[2]/16384:.1f}\n')
    #lcd.putstr(f'X:{gyro[0]/131:2.0f} Y:{gyro[1]/131:2.0f} Z:{gyro[2]/131:2.0f}')
    time.sleep(0.2)

