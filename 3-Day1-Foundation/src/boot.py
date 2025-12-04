#
#
import network
import time
import ntptime

SSID = 'xxxx'
PASSWD = 'yyyyy'

MAX_RETRY = 10
station = None

def setup_WiFi(id, pwd):
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.connect(id, pwd)
    while sta.isconnected() == False:
        time.sleep(1)
        retry_count += 1
        if retry_count > MAX_RETRY:
            print('Connection failed')
            return None, False
    print('Connection successful')
    print(sta.ifconfig())
    return sta, True

sta, stat = setup_WiFi(SSID, PASSWD)

if stat:
    # Synchronize system clock using NTP
    # Wait briefly to ensure DNS is ready
    time.sleep(3)

    # Try synchronizing  system clock by  NTP
    try:
        ntptime.settime()
        print("Time synchronized:", time.localtime())
    except OSError as e:
        print("NTP sync failed:", e)

#
# import micropython shell
#from upysh import *
#
#