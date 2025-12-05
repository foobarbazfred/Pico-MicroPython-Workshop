# 無線通信

### Raspberry Pi Pico 2 WのWifi機能

Raspberry Pi Pico ２ Wには無線機能が搭載されており、Wi-FiやBLEを使うことができます。本講義ではWi-Fiを使ったプログラミングを行います。Wi-Fiネットワークと接続するためのモジュールが提供されています。

boot.pyの全コードは以下を参照ください<br>
[src/boot.py](src/boot.py)
<br>

WiFiに接続するコードの例は以下

Wi-Fi接続サンプル
```
#
#
import network
import time

SSID = 'xxxxx24G'
PASSWD = 'xxxxx'

def setup_WiFi(id, pwd):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(id, pwd)
    time.sleep(1)
    if station.isconnected() == True:
        print('Connection successful')
        print(station.ifconfig())
    else::
        print('Connection failed')

setup_WiFi(SSID, PASSWD)
```
上記認証が正しく行えるとDHCPによりIPが割り当てられます。
上記プログラムではstation.ifconfig()によりIPを表示させています。例えば以下
```
Connection successful
('192.168.10.52', '255.255.255.0', '192.168.10.1', '8.8.8.8')
```
先頭のIPが割り当てられたIP,続いて、サブネットマスク、デフォルトGWのIP、DNSサーバのIPとなっています。

なお、WiFIは2.5GHz帯のみ使えるようです

ネットワーク通信ではSSL通信が使われます。SSL通信では接続先サーバの証明書を取得し、偽装したサイトでないかを確認します。この時、証明書の有効期限が適切であるか？証明書の有効期限を確認します。このため、SSL通信のクライアント側では正しい時刻設定がなされている必要があります。
インターネット上では時刻同期サービスが提供されており、時刻同期用モジュールを使うことで、簡単に時刻同期が行えます。
時刻同期のサンプルコードは以下です
```
import time
import ntptime

# Synchronize system clock using NTP
# Wait briefly to ensure DNS is ready
time.sleep(3)

# Try synchronizing  system clock by  NTP
try:
    ntptime.settime()
    print("Time synchronized:", time.localtime())
except OSError as e:
    print("NTP sync failed:", e)
```
IPを取得してすぐに時刻同期するとエラーになる場合があるため、Workaround用として、time.sleep(3)を入れています。コードを打つことで正しく同期できかどうかを確認できます
```
import time
time.localtime()
```
以下の表示がされます。2025/12/3 7:43:14  (UTCなので、日本時間で+9の16時43分)
```
(2025, 12, 3, 7, 43, 14, 2, 337)
```

boot.pyの全コードは以下を参照ください<br>
[src/boot.py](src/boot.py)
<br>
