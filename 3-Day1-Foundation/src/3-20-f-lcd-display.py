#
# file: 3-20-f-lcd-display.py
# 機能：I2C接続のキャラクタ液晶ディスプレイ(16×2)を初期化し、文字列を表示するサンプル
#
from machine import Pin
from machine import I2C
from I2C_LCD import I2CLcd
LCD_ADDR = 0x27

i2c_1 = I2C(1, scl=Pin(19), sda=Pin(18), freq=40_000)
lcd = I2CLcd(i2c_1, LCD_ADDR, 2, 16)
lcd.putstr('hello')
