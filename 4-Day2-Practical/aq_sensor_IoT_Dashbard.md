# 空気質収集とIoTダッシュボード表示(その１）

## 要件
- システム名
  -  遠隔空気質見えるかシステム 
- できること
  - 遠隔地に配置した空気質センサを用いて温度、湿度、CO2濃度をリアルタイムで表示する
  - ダッシュボード形式でグラフ化して見やすくする

## システム構成
<img src="assets/IAQ_sensing_archi.png" width=800>
 

### ソース(Raspberry Pi Pico 2 W)
空気質センサで温度、湿度、CO2濃度を収集し、MQTTでPublishする

動作例
```
temp: 25.28C, hum: 19.47 %, CO2: 506 ppm
send message {"hum": 19.465934, "co2": 506, "temp": 25.275048} on topic handson/sensor/volume/user001
```

```
import time
from scd41 import *

# Sensor I2C Connection Pin Assign
I2C_SDA = 4
I2C_SCL = 5

# mqtt defines
import json
from umqtt.simple import MQTTClient

# define MQTT Broker
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_BASE = "handson/sensor/volume/user"
MEMBER_ID = 1
CLIENT_ID = f'rpi_pico_{MEMBER_ID:03d}'
TOPIC = TOPIC_BASE + f"{MEMBER_ID:03d}"

def connect():
    print(f'Connected to MQTT Broker {BROKER}')
    client = MQTTClient(CLIENT_ID, BROKER, PORT)
    client.connect()
    return client

def reconnect():
    print(f'Failed to connect to MQTT broker {BROKER}, Reconnecting...')
    time.sleep(5)
    client.reconnect()

def mqtt_publish(temp, hum, co2):
    msg = json.dumps({'temp': temp, 'hum' : hum , 'co2' : co2})
    print('send message %s on topic %s' % (msg, TOPIC))
    client.publish(TOPIC, msg, qos=0)

client = None
def main():
    global client
    try:
        client = connect()
    except OSError as e:
        reconnect()


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
            mqtt_publish(temp, hum, co2)
        time.sleep(60)

if __name__ == '__main__':    
   main()    

#
# end of file
#
```
