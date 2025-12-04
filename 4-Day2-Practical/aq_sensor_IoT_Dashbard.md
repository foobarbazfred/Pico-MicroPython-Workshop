# 空気質収集とIoTダッシュボード表示


センサで空気質情報を収集し、MQTTでPublishする

```
from scd41 import *

# Sensor I2C Connection Pin Assign
I2C_SDA = 4
I2C_SCL = 5

def main():

    #
    # setup
    #
    
    # setup i2c bus for sensor
    i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=20_000)
    
    # >>> hex(i2c.scan()[0])
    # '0x62'
    
    init_sensor(i2c)
    time.sleep(5)        # wait until sensor is ready

    #
    # loop
    #
    
    while True:
        temp, hum, co2 = read_measurement(i2c)
        if temp is None:
            print(f"temp: --.-- C, hum: --.-- %, CO2: ---- ppm")           
        else:
            print(f"temp: {temp:.2f}C, hum: {hum:.2F} %, CO2: {co2} ppm")
        time.sleep(60)

if __name__ == '__main__':    
   main()    
```
