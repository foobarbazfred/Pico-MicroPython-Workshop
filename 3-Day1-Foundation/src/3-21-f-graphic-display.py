#
# file: 3-21-f-graphic-display.py
# 機能：SPI接続のグラフィックディスプレイ(ST7735)を初期化し、
# 塗りつぶし・図形・テキストを描画するサンプル
#

#
# test program for Graphic Display with ST7735 Driver 
# original source is https://github.com/mcauser/micropython-st7735/blob/master/test.py
#

# GP8  SPI1 Rx
# GP9  SPI1 CSn
# GP10 SPI1 SCK
# GP11 SPI1 TX
# GP12 A0 
# GP13 CS
# GP14 RESET

import time
from machine import Pin
from machine import SPI
from st7735r import ST7735R

#
# Color defines (RGB565)
#
COLOR_BLACK = 0x0000
COLOR_WHITE = 0xFFFF
COLOR_RED = 0xF800
COLOR_GREEN = 0x07E0
COLOR_BLUE = 0x001F
COLOR_CYAN = 0x07FF
COLOR_MAGENTA = 0xF81F
COLOR_YELLOW = 0xFFE0

#
# LCD size defines (128 x 160)
#
TFT_WIDTH = 128
TFT_HEIGHT = 160

#
# Pin assigns
#
TFT_SPI_BAUD = 800_0000   #800Kbps
TFT_SPI_MOSI = 11
TFT_SPI_MISO = 8
TFT_SPI_SCK = 10

TFT_DC = 12
TFT_CS = 13
TFT_RST = 14

mosi  = Pin(TFT_SPI_MOSI, Pin.OUT)
miso  = Pin(TFT_SPI_MISO, Pin.OUT)
sck  = Pin(TFT_SPI_SCK, Pin.OUT)

rst  = Pin(TFT_RST, Pin.OUT)
cs  = Pin(TFT_CS, Pin.OUT)
dc  = Pin(TFT_DC, Pin.OUT)

spi = SPI(1, baudrate=TFT_SPI_BAUD, polarity=1, phase=1, mosi=mosi, miso=miso, sck=sck )

#
# workaround code from https://github.com/mcauser/micropython-st7735/blob/master/test.py
#
# spi = SPI(1, baudrate=8000000, polarity=1, phase=0) # green tab works, blue does not
# spi = SPI(1, baudrate=8000000, polarity=0, phase=0) # both blue and green tab work
# spi = SPI(1, baudrate=8000000, polarity=0, phase=1) # blue works, green does not

#
#  create and initialize tft instance
#
tft = ST7735R(spi, dc, cs, rst, w=TFT_WIDTH, h=TFT_HEIGHT, x=0, y=0, rot=0, inv=False, bgr=False)
tft.init()

#
# fill color test
#
time.sleep(1)
tft.fill(COLOR_BLACK)
time.sleep(1)
tft.fill(COLOR_WHITE)
time.sleep(1)

for _ in range(3):
    for color in (COLOR_RED, COLOR_GREEN, COLOR_BLUE):
          tft.fill(color)
          time.sleep(1)

#
# draw graphics
#
tft.fill(COLOR_BLACK)
tft.rect_outline(0, 0, TFT_WIDTH, TFT_HEIGHT, COLOR_BLUE)
tft.line(0, 0, TFT_WIDTH, TFT_HEIGHT, COLOR_RED)
tft.line(TFT_WIDTH, 0, 0, TFT_HEIGHT, COLOR_GREEN)

if TFT_WIDTH < TFT_HEIGHT:
   radius = int(TFT_WIDTH/2)
else:
   radius = int(TFT_HEIGHT/2)
tft.circle_outline(int(TFT_WIDTH/2),int(TFT_HEIGHT/2),radius,COLOR_CYAN)

tft.line(10, 10, int(TFT_WIDTH/2), int(TFT_HEIGHT/2), COLOR_RED)

import terminalfont
(pos_x, pos_y) = ( int(TFT_WIDTH/4), int(TFT_HEIGHT/5))

tft.text(pos_x, pos_y, 'Hello,', terminalfont, COLOR_WHITE, size=1)
tft.text(pos_x + 10, pos_y + 10, 'World!!', terminalfont, COLOR_WHITE, size=1)

