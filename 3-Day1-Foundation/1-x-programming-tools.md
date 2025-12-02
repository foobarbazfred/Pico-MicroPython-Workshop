# プログラミングの方法


### メンテナンスツール(CLI)
MicroPython のリモート制御: mpremote<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/reference/mpremote.html#micropython-remote-control-mpremote

### コマンド例

RP2のFlash上に実現されているファイルシステム内の/lib配下のファイルを一覧表示
```
$ python3 -m mpremote connect /dev/ttyS17  fs ls :/lib
ls :/lib
        3164 I2C_LCD.py
        6536 LCD_API.py
        1448 hc_sr04.py
           0 mfr522.py
       16758 mfrc522.py
        5250 mpu6050.py
         428 mylib.py
           0 neopixel.pyb
        3009 neopixel2.py
        9959 sdcard.py
        2824 upysh.py
```
```
   for file in  I2C_LCD.py LCD_API.py hc_sr04.py mfrc522.py mpu6050.py mylib.py neopixel2.py sdcard.py upysh.py 
do
  echo $file
  echo "python3 -m mpremote connect /dev/ttyS17  fs cp :/lib/$file  ./lib/$file"
  python3 -m mpremote connect /dev/ttyS17  fs cp :/lib/$file  ./lib/$file
done   
```
一括転送の例
```
python3 -m mpremote connect /dev/ttyS17  fs cp -r  ./lib  :/lib
```
