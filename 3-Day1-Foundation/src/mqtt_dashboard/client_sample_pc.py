#!/usr/bin/python3

#
# MQTT Client Sample for PC (using paho mqtt)
#


import paho.mqtt.client as mqtt
import json
import random
import time

# MQTT Broker設定（EMQX/TCP接続(MQTT)）
BROKER = "broker.emqx.io"
PORT = 1883
TOPIC_BASE = "handson/sensor/volume/user"

# MQTTクライアント初期化
client = mqtt.Client()

# 接続時のコールバック
def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)

client.on_connect = on_connect
client.connect(BROKER, PORT, 60)

# メインループ：乱数をPublish
try:
    while True:
        value = random.randint(1, 100)  # 1〜100の乱数
        id = random.randint(1,16)
        topic = TOPIC_BASE + f"{id:03d}"
        payload = json.dumps({"value": value})
        client.publish(topic, payload)
        print(f"Published to {topic}: {payload}")
        time.sleep(0.5)  # 0.5秒ごとに送信
except KeyboardInterrupt:
    print("Stopped by user")
    client.disconnect()
