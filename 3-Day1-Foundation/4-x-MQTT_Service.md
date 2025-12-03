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

- 接続先ブローカ：
- TOPICS：
- message: 

1秒おきにMQTTブローカにメッセージを送信する例です
```
from umqtt.simple import MQTTClient
import json

MQTT_BROKER = 'test.mosquitto.org'
MQTT_PORT = 1883
MQTT_TOPIC = b'test/upy_publish_test'
MQTT_CLIENT_ID = "client_RP_Pico2W_0001"

client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port = MQTT_PORT, ssl = False)
client.connect()
message = {‘client_id’ : MQTT_CLIENT_ID, ‘connect by’ : ‘no SSL, no Auth’}
payload = json.dumps(message). encode('utf-8')
while True:
    client.publish(MQTT_TOPIC, payload)
    time.sleep(1)
client.disconnect()
```

   
