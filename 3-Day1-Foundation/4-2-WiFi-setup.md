# 4-2 Raspberry Pi Pico 2 Wの無線通信

Raspberry Pi Pico 2 W(Pico2W)にはWi-Fiによる通信や、Bluetoothによる通信が可能です。この章ではインターネットと接続が可能になるWi-Fi接続について説明します。

### Pico2WのWi-Fi機能

本章ではWi-Fiを使ったプログラミングを行います。Wi-Fiネットワークと接続するためのライブラリが提供されています。
```
network.WLAN(network.STA_IF)
```
WiFiに接続するコードを以下に示します。下記は分かりやすいように、接続完了まで一定時間待つ簡略版です。接続完了まで指定された回数リトライするバージョンは下記リンクのboot.pyを参照してください。

```
#
# Wi-Fi 接続サンプル(簡易版)
#
import network
import time

SSID = 'xxxxx24G'
PASSWD = 'xxxxx'

def setup_WiFi(id, pwd):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(id, pwd)
    time.sleep(1)            # TODO: Avoid fixed 1-second delay; needs improvement
    if station.isconnected() == True:
        print('Connection successful')
        print(station.ifconfig())
    else:
        print('Connection failed')

setup_WiFi(SSID, PASSWD)
```
上記認証が正しく行えるとDHCPによりIPが割り当てられます。
上記プログラムではstation.ifconfig()によりIPを表示させています。例えば以下
```
Connection successful
('192.168.10.52', '255.255.255.0', '192.168.10.1', '8.8.8.8')
```
先頭のIPが割り当てられたIP,続いて、サブネットマスク、デフォルトGWのIP、DNSサーバのIPとなっています。なお、Pico2WのWi-Fiは2.4GHz帯のみ使えるようです

リトライ回数を指定したboot.pyの全コードは以下を参照ください<br>
[src/boot.py](src/boot.py)

###　NTPによる時刻同期

ネットワーク通信ではSSL通信が使われます。SSL通信では接続先サーバの証明書を取得し、偽装したサイトでないかを確認します。この時、証明書の有効期限が適切であるか？証明書の有効期限を確認します。このため、SSL通信のクライアント側では正しい時刻設定がなされている必要があります。
インターネット上では時刻同期サービスが提供されており、時刻同期用モジュールを使うことで、簡単に時刻同期が行えます。
時刻同期のサンプルコードは以下です

```
#
# 機能：NTPによる時刻同期サンプルコード
#
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
IPを取得してすぐに時刻同期するとエラーになる場合があるため、Workaround用として、time.sleep(3)を入れています。time.localtime()を実行することで正しく時刻同期できているかを確認できます
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

### ネットワーク経由でモジュールをインストールする方法
Pico2Wをネットワークに接続することで、モジュールのインストールもネットワーク経由で行うことが可能になります。ネットワーク経由でモジュールをインストールするには、mipモジュールを使用します。リポジトリに登録されているモジュールであれば、モジュール名を指定して、`mip.install(<ライブラリ名>)`を実行することで、指定したライブラリがネットワーク経由でインストールされます。
```
import mip
mip.install(<ライブラリ名>)
```
リポジトリに登録されておらずGitHubでソースが公開されている場合、ソースのパスを指定して`mip.install()`を実行します。
```
import mip
mip.install(<ソースが公開されているURLパス>)
```

