# プログラミングの方法


### メンテナンスツール(CLI)
MicroPython のリモート制御: mpremote<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/reference/mpremote.html#micropython-remote-control-mpremote

### コマンド例
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
