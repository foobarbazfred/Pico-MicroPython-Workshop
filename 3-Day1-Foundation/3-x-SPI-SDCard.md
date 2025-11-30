# SDカードの接続

SPIを用いてSDカードと接続することができます。SDカードには＃＃＃モードと、SPIモードがあり、SDカードの動作モードをSPIモードに切り替えて接続します。SDカードとのやり取りはSDカード用ドライバが提供されており、SDカード用ドライバを用いることで、数行のコードを書くだけでSDカードが利用可能になります。

SDカードを利用する上で、注意点があります。MicroPythonのファイルシステムでは、扱えるメディアのフォーマットがFAT12、FAT16、FAT32のいずれかである必要があります。exFATは扱えないので、exFATでフォーマットされたSDカードは読めません。６４GB以上の容量になるとexFATによるフォーマットが一般的ですので、６４GB以上のSDカードを読み書きする場合、ツールを使ってSDカードのフォーマットをFAT32でフォーマットしなおす必要があります。

今回の試作では、2つあるHW SPIのうち、 Channel 1 を使っています。Channel 1のデフォルトピンアサインは、CLK:#, MOSI:#, MISO:# です。指定しなくても、SPI(1)とすると上記ピンが割り当てられますが、確実にピンが割り当てられるよう冗長ですが明示しています。

### 配線図
<img src="assets/spi_sd_card_schematics.png" width=700>

SDカード接続テスト
```
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
cs = machine.Pin(SD_CARD_CS, Pin.OUT, pull=Pin.PULL_UP)
spi1 = SPI(1, baudrate=SPI_BAUD, sck=Pin(SPI_SCK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO))

# init SDCard Driver
sd = sdcard.SDCard(spi=spi1, cs=cs)

# mount SD Card Volume to /sd
os.mount(sd, '/sd')
os.listdir('/sd')

# umount SD Card Volume
#os.umount('/sd')
```

### 参考資料
- Sensirion SDC41 Porcut
  - https://sensirion.com/jp/products/catalog/SCD41
- Sensirion SCD4x DataSheet
  - https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf
- Sensirion Drvier
  - https://github.com/Sensirion/python-i2c-scd/tree/master/sensirion_i2c_scd/scd4x


### SD Card Driver
https://github.com/micropython/micropython-lib/blob/master/micropython/drivers/storage/sdcard/sdcard.py
