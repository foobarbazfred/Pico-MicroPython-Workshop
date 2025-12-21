# グラフィックディスプレイの利用

マイコンと接続して描画できる安価なグラフィックディスプレイがいろいろ販売されています。いろんな種類のディスプレイがありますので、必要な画素数やサイズから選んでください。MicroPythonからグラフィックディスプレイに描画するには、ディスプレイコントローラに描画の命令を送る必要があります。具体的には、ディスプレイコントローラのレジスタに対して必要な情報を書き込むことで描画が可能になります。スクラッチで作るのは大変なので、他の人が開発、リリースしてくれているディスプレイコントローラ用のドライバを用います。使いたいグラフィックディスプレイに実装されているディプレイコントローラは何を使っているのかを特定して、該当するディスプレイコントローラ用のドライバをMicroPythonにインストールします。ユーザプログラムではドライバをimport して、ドライバ経由でディスプレイを制御することで、グラフィック描画やテキストの描画が容易に行えます。

本章ではディプレイコントローラ：ST7735を使ったグラフィックディスプレイを取り上げます。ST7735はSPIで制御します。

### ST7735用ドライバとフォント
ST7735用ドライバとして、boochow氏が公開されているドライバを使います。（他の方もST7735用にいろいろ公開されていますが、boochow氏作のドライバが安定して動作するので選んでいます。）
ソースは以下に置かれています<br>
https://github.com/boochow/MicroPython-ST7735/tree/master<br>
mipモジュールのinstall機能を使ってドライバをインストールできます。
```
import mip
mip.install('https://raw.githubusercontent.com/boochow/MicroPython-ST7735/refs/heads/master/ST7735.py')
```
上記操作で、Raspberry Pi Pico 2 WのFlashメモリの/lib配下にST7735.pyがインストールされます。<br>
上記ドライバは、ST7735を制御して直線や曲線等のグラフィック描画が可能になります。もしグラフィックディプレイに文字を出す場合は、フォントデータが必要になります。フォントデータはかつてGuyGarver氏のリポジトリ(下記)から入手できていましたが、現在はPublicはリポジトリはすべて閉鎖されたようです。<br>
https://github.com/GuyCarver/MicroPython/tree/master/lib<br>
GuyGarver氏のソースをベースにした新しいterminalfont.pyがmcauser氏によって公開されておりこれを使うことでテキスト描画が可能です<br>
https://github.com/mcauser/micropython-st7735/tree/master<br>
フォントデータは以下でインストールできます
```
import mip
mip.install('https://raw.githubusercontent.com/mcauser/micropython-st7735/refs/heads/master/terminalfont.py')
```
### ディスプレイの接続と描画テスト
RP2とディスプレイはSPIで接続します。必要な結線は、SPI_SCK, SPI_TX, A0(Command/Data Selector), CS, RESETです。出力用デバイスということで、HW SPIチャンネルの2番目(SPI1)用のピンを使っています。ピンの割り当てはご都合に合わせて変更可能です。
簡単なテストプログラムを示します。画面の塗りつぶしと斜線を表示します。
```
#
# test program for ST7735
#

# GP8  SPI1 Rx
# GP9  SPI1 CSn
# GP10 SPI1 SCK
# GP11 SPI1 TX
# GP12 A0 
# GP13 CS
# GP14 RESET


from ST7735 import TFT
#from sysfont import sysfont
from machine import SPI
from machine import Pin
import time

PIN_ADC=12
PIN_CS=13
PIN_RESET=14

SPI1_BAUD=12_000_000
PIN_SPI1_SCK=10
PIN_SPI1_TX=11
PIN_SPI1_RX=8

spi = SPI(1, baudrate=SPI1_BAUD, sck=Pin(PIN_SPI1_SCK), mosi=Pin(PIN_SPI1_TX), miso=Pin(PIN_SPI1_RX))
tft=TFT(spi, PIN_ADC, PIN_RESET, PIN_CS)


#
#
#
tft.initr()
tft.rgb(True)

#
# fill test
#
for _ in range(5):
    for color in (TFT.WHITE, TFT.BLUE, TFT.FOREST, TFT.RED, TFT.BLACK):
        tft.fill(color)
        time.sleep(0.5)

#
# draw lines
#
WIDTH,HEIGHT=tft.size()
tft.line((0,0),(WIDTH,HEIGHT),TFT.WHITE)
tft.line((WIDTH,0),(0,HEIGHT),TFT.WHITE)

#
# clear screen
#
time.sleep(5)
tft.fill(TFT.BLACK)
```
フォントデータをインストールすることで、テキストの描画が可能になります。以下はテキスト(Hello, World!)の描画サンプルです。
```
#
# test program for ST7735
#

# GP8  SPI1 Rx
# GP9  SPI1 CSn
# GP10 SPI1 SCK
# GP11 SPI1 TX
# GP12 A0 
# GP13 CS
# GP14 RESET

from ST7735 import TFT
from terminalfont import terminalfont
from machine import SPI
from machine import Pin
import time

PIN_ADC=12
PIN_CS=13
PIN_RESET=14

SPI1_BAUD=12_000_000
PIN_SPI1_SCK=10
PIN_SPI1_TX=11
PIN_SPI1_RX=8

spi = SPI(1, baudrate=SPI1_BAUD, sck=Pin(PIN_SPI1_SCK), mosi=Pin(PIN_SPI1_TX), miso=Pin(PIN_SPI1_RX))
tft=TFT(spi, PIN_ADC, PIN_RESET, PIN_CS)

#
#
#
tft.initr()
tft.rgb(True)
tft.fill(TFT.BLACK)
    
WIDTH,HEIGHT=tft.size()
tft.text((int(WIDTH/6), int(HEIGHT/2)), "Hello, World!", TFT.WHITE, terminalfont, 1, nowrap=True)

#
#
#
```

### ST7735以外のディプレイコントローラについて

ディスプレイの種類によって、ST7735以外にST7789やILI9341等のコントローラが使用されています。その場合は、MicroPython版の各コントローラ用ドライバを探してください。もしMicroPython版ドライバが存在しない場合はArduino版ドライバを探すと見つかる場合があります。Arduino版ドライバはC/C++で実装されていますので、MicroPythonで動くように書き換えて開発してください。書き換えのポイントとしては、コントローラのどのレジスタにどのような値設定しているかを確認してMicroPythonで実装する作業になります。コントローラのハードウエア仕様書も入手可能な場合が多いので、ハードウエア仕様書とドライバソースを一緒に読むとコントローラをどのように制御したら良いのか理解が深まると思います。

### ご参考
他の6x8フォント<br>
https://github.com/idispatch/raster-fonts/blob/master/font-6x8.c<br>

