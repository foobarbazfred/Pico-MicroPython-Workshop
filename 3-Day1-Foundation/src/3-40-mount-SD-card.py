#
# file : 3-40-mount-SD-card.py
# 機能：SPIでSDカードを制御し、/sd ディレクトリにマウントする
#
import os
from machine import Pin
from machine import SPI
import sdcard

SPI_MISO = 8
SD_CARD_CS = 9
SPI_SCK = 10
SPI_MOSI = 11
SPI_BAUD = 1_000_000  # 1MHz
#
# setup
#
cs = Pin(SD_CARD_CS, Pin.OUT, pull=Pin.PULL_UP)
spi1 = SPI(1, baudrate=SPI_BAUD, sck=Pin(SPI_SCK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO))

# init SDCard Driver
sd = sdcard.SDCard(spi=spi1, cs=cs)

# mount SD Card Volume to /sd
os.mount(sd, '/sd')
os.listdir('/sd')

# umount SD Card Volume
#os.umount('/sd')
