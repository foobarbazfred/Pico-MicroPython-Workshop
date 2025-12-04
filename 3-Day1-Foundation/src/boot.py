#
#
import network
import time
import ntptime

SSID = 'xxxxx24G'
PASSWD = 'xxxxx'

MAX_RETRY = 10
station = None

def setup_WiFi(id, pwd):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(id, pwd)
    while station.isconnected() == False:
        time.sleep(1)
        retry_count += 1
        if retry_count > MAX_RETRY:
            print('Connection failed')
            return None, False
    print('Connection successful')
    print(station.ifconfig())
    return station, True

station, status = setup_WiFi(SSID, PASSWD)

if status:
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
