#
# file: 3-7-f-motion-sensor.py
# 機能：6軸モーションセンサ(MPU6050)から加速度と角速度を読み取り、シリアルコンソールに表示するサンプル
#
from mpu6050 import MPU6050
import time

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
    time.sleep(1)

