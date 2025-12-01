#
#
import network
import time
import ntptime

SSID = 'xxxxx24G'
PASSWD = 'xxxxx'

def setup_WiFi(id, pwd):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(id, pwd)
    while station.isconnected() == False:
        pass

    print('Connection successful')
    print(station.ifconfig())

setup_WiFi(SSID, PASSWD)

# Synchronize system clock using NTP
# Wait briefly to ensure DNS is ready
time.sleep(3)

# Try synchronizing  system clock by  NTP
try:
    ntptime.settime()
    print("Time synchronized:", time.localtime())
except OSError as e:
    print("NTP sync failed:", e)

from upysh import *
#
#
#
