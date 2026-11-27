#
# file: 3-11-f-arducam-sample.py
# 機能：Arducam(OV5642)を使って撮影し、バッファに格納するサンプル（表示機能なし）
#
from machine import Pin
from machine import I2C
from machine import SPI
from ov5642 import OV5642

ov5642i2c = I2C(scl=Pin(5), sda=Pin(4), freq=9600)

CAM_PIN_CS = 1
fifo_cs = Pin(CAM_PIN_CS, Pin.OUT)

SPI0_BAUDRATE=10_00_000
SPI0_MOSI = 3
SPI0_MISO = 0
SPI0_SCK = 2
fifo_spi = SPI(0,SPI0_BAUDRATE,sck=Pin(SPI0_SCK), mosi=Pin(SPI0_MOSI), miso=Pin(SPI0_MISO))
ardu = OV5642(ov5642i2c, fifo_spi, fifo_cs)

SCREEN_WIDTH=160
SCREEN_HEIGHT=128
BYTEPERPIX=2  # RGB565

import gc
gc.collect()
buf = bytearray(SCREEN_WIDTH * SCREEN_HEIGHT * BYTEPERPIX)

ardu.fifo.clear_done_flag()       
ardu.fifo.start_capture_and_wait()
ardu.read_pixels(buf)
