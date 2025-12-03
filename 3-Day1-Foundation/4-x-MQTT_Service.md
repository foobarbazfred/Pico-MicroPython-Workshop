# MicroPythonからMQTTサービスを使う


MQTT(Message Queuing Telemetry Transport)を使うことで、複数拠点に配置したセンサデータの収集や、家庭内に設置した機器を遠隔から制御するアプリケーションが容易に実現できます。MicroPython 用のMQTTライブラリも存在し、MQTTを活用したアプリケーションを簡単につくることができます。
MicroPython用MQTTライブラリはリポジトリに登録されており、MicroPythonのMIPによりネットワーク経由でインストールすることができます。
1. まずmipモジュールをインポートします(REPL)
```
import mip
```
2. mip.install()関数を用いてumqtt.simpeをインストールします
```
mip.install(‘umqtt.simple’)
```
上記操作によりMicroPythonのFlash(ファイルシステム)にumqtt.simpleがインストールされます。
以下は実行結果です
```
>>> import mip
>>> dir(mip)
['__class__', '__name__', 'const', '__dict__', '__file__', '__path__', 'sys', '_CHUNK_SIZE', '__version__', '_check_exists', '_chunk', '_download_file', '_ensure_path_exists', '_install_json', '_install_package', '_rewrite_url', 'allowed_mip_url_prefixes', 'install', 'requests']
>>> mip.install('umqtt.simple')
Installing umqtt.simple (latest) from https://micropython.org/pi/v2 to /lib
Copying: /lib/ssl.mpy
Copying: /lib/umqtt/simple.mpy
Done
```
ファイルが置かれたか確認します。以下の操作により、 Flash上のファイルシステム内、/lib/umqtt/simple.mpy' が置かれたことが分かります
```
>>> ls('lib')
    <dir> umqtt
      745 ssl.mpy
     2824 upysh.py
2,504k free
>>> ls('lib/umqtt')
     2529 simple.mpy
2,504k free
```

### MQTTライブラリを使ったPublishの例

まずは簡単に定期的にメッセージを発行するテストを行います。

- 接続先ブローカ：broker.emqx.io
- ポート番号：1883
- TOPICS： handson/sensor/volume/<user_ID>     #   <user_id>  := 受講者ID（1-16)
- message: {"value" : ＜value＞ }               # ＜value＞ := 0 - 100

1秒おきにMQTTブローカにメッセージを送信する例です.
```
#
# MQTT Publish Sample
#   publish random value
# 
import time
import random
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
    print('Connected to MQTT Broker "%s"' % (server))
    client = MQTTClient(CLIENT_ID, BROKER, PORT)
    client.connect()
    return client

def reconnect():
    print('Failed to connect to MQTT broker, Reconnecting...' % (server))
    time.sleep(5)
    client.reconnect()

# setup

try:
    client = connect()
except OSError as e:
    reconnect()

# loop

while True:
   value = random.randint(1, 100)  # random number 1-100
   msg = json.dumps({"value": value})
   print('send message %s on topic %s' % (msg, TOPIC))
   client.publish(TOPIC, msg, qos=0)
   time.sleep(1)

#
# end of source
#
```
本当に送信できているのか？を確認するためのIoTダッシュボードのサンプルは以下です。ダウンロードしてブラウザで開いてください。<br>


<img src="assets/mqtt_dashboard.png" width=600>
   
