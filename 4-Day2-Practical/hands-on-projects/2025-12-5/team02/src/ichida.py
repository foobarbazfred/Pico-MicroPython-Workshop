from machine import Pin
from machine import I2C
from I2C_LCD import I2CLcd
from scd41 import *
import time
import json
from umqtt.simple import MQTTClient

LCD_ADDR = 0x27

# CO2 senser init
I2C_SCD41_SDA = 4
I2C_SCD41_SCL = 5
i2c = I2C(0, scl=Pin(I2C_SCD41_SCL), sda=Pin(I2C_SCD41_SDA), freq=20_000)
# >>> hex(i2c.scan()[0])
# '0x62'
init_sensor(i2c)
time.sleep(5)

# define MQTT Broker
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_BASE = "handson/sensor/volume/user"
MEMBER_ID = 3
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
try:
    client = connect()
except OSError as e:
    reconnect()

# lcd init
i2c_1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=40_000)
lcd = I2CLcd(i2c_1, LCD_ADDR, 2, 16)
lcd.clear()
lcd.move_to(0, 0)   # clearすると0,0に設定されます
lcd.putstr("## ICHIDAgaki ##")
lcd.move_to(0, 1)   # clearすると0,0に設定されます
lcd.putstr("#### Maker  ####")

while True:
    temp, hum, co2 = read_measurement(i2c)
    # print_Window
    if temp is None:
        print(f"temp: --.-- C, hum: --.-- %, CO2: ---- ppm")           
    else:
        print(f"temp: {temp:.2f}C, hum: {hum:.2F} %, CO2: {co2} ppm")
    if 15 <= temp <= 25:
        temp_j = "OK"
    else:
        temp_j = "NG"
    if 30 <= hum <= 50:
        hum_j ="OK"
    else:
        hum_j = "NG"
    
    lcd.clear()         # print LCD
    lcd.move_to(0, 0)   # clearすると0,0に設定されます
    lcd.putstr(f"Tmp:{temp:.1f}C -> " + temp_j)
    lcd.move_to(0, 1)   # clearすると0,0に設定されます
    lcd.putstr(f"Hum:{hum:.1F}% -> " + hum_j)
    
    # MQTT
    msg = json.dumps({"Temp": temp,"Hum": hum})
    print('send message %s on topic %s' % (msg, TOPIC))
    client.publish(TOPIC, msg, qos=0)
    
    time.sleep(5)
    
    
