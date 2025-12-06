#
# MQTT Publish Sample
#   publish random value
# 
import time
import random
import json
from umqtt.simple import MQTTClient
from scd41 import read_measurement
from machine import I2C, Pin

# define MQTT Broker
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_BASE = "env_control/sensor/room"
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

# setup

try:
    client = connect()
except OSError as e:
    reconnect()

# loop

I2C_SDA = 4
I2C_SCL = 5
i2c = I2C(0, scl=Pin(I2C_SCL), sda=Pin(I2C_SDA), freq=20_000)

from neopixel2 import myNeopixel
NUM_LEDS = 8
PIN_NO = 3
np = myNeopixel(NUM_LEDS, PIN_NO)

LED_MAX = 100

co2_min = 1000
co2_max = 4000
co2_pos = 4

temp_min = 20
temp_max = 30
temp_pos = 0

hum_min = 25
hum_max = 75
hum_pos = 2

"""
センサの取得値をLEDの赤色（%）に変換する関数
minとmaxが閾値、ledはデフォルトで100
"""
def m2led(min, max, value, led = 100):
    if value is not None:
        value = value if value <= max else max
        value = value if value >= min else min
    else:
        value = (max + min) / 2
    return (value - min) * led / (max - min)

while True:
   temp, hum, co2 = read_measurement(i2c)  # random number 1-100
   msg = json.dumps({"temp": temp, "hum": hum, "co2": co2})
   print('send message %s on topic %s' % (msg, TOPIC))
   client.publish(TOPIC, msg, qos=0)
   n_co2 = m2led(co2_min, co2_max, co2)
   n_temp = m2led(temp_min, temp_max, temp)
   n_hum = m2led(hum_min, hum_max, hum)
   np.set_pixel(co2_pos, n_co2, 100 - n_co2, 0)
   np.set_pixel(temp_pos, n_temp, 100 - n_temp, 0)
   np.set_pixel(hum_pos, n_hum, 100 - n_hum, 0)
   np.show()
   time.sleep(5)

#
# end of source
#
