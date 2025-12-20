# グラフィックディスプレイの利用

SPIバスを使って制御できる安価なグラフィックディスプレイが販売されています。いろんな種類のディスプレイがありますので、必要な画素数やサイズから選んでください。MicroPythonから制御するには、ディプレイコントローラとして何を使っているのかを特定して、該当のディスプレイコントローラ用のドライバをMicroPythonにインストールします。ユーザプログラムではドライバをimport して、ドライバ経由でディスプレイを制御することで、グラフィック描画やテキストの描画が容易に行えます。

本章ではディプレイコントローラ：ST7735を使ったグラフィックディスプレイを取り上げます。ST7735以外にもST7789やILI9341等のドライバが使われる場合があります。その場合は、MicroPython版の各ドライバを探してみてください。もしMicroPython用ドライバが存在しない場合はArduino用ドライバを探すと見つかる場合があります。Arduino用ドライバはC/C++で実装されていますので、MicroPython用にポーティングしてください。ポイントとしては、コントローラのどのレジスタにどのような値設定しているかを確認してポーティングすることになると思います。コントローラのハードウエア仕様書も入手可能な場合が多いので、ドライバソースとハードウエア仕様書を一緒に読むと理解が深まると思います。

### ST7735用ドライバとフォント
ST7735用ドライバとして、boochow氏が公開されているドライバを使います。（他の方もST7735用にいろいろ公開されていますが、boochow氏作のドライバが安定して動作するので選んでいます。）
ソースは以下に置かれています<br>
https://github.com/boochow/MicroPython-ST7735/tree/master<br>
mipモジュールのinstall機能を使ってドライバをインストールできます(未テスト)
```
import mip
mip.imstall('https://raw.githubusercontent.com/boochow/MicroPython-ST7735/refs/heads/master/ST7735.py')
```
上記ドライバは、ST7735を制御する機能だけが実装されており、直線や曲線等のグラフィック描画のみであれば上記ドライバで実現できます。もしディプレイに文字を出す場合は、フォントが必要になります。かつてフォントはGuyGarver氏のリポジトリ(下記)から入手できていましたが、現在はPublicはリポジトリはすべて閉鎖されたようです。<br>
https://github.com/GuyCarver/MicroPython/tree/master/lib<br>
fontなしではテキスト表示できないので、公開当時に入手したフォントを仮に以下に置いています。公開当時も使用許諾については記載がありませんでした。もし使用許諾が明記された代替えフォントが入手できればあればそちらに置き換えます。

### ディスプレイの接続と描画テスト
RP2とディスプレイはSPIで接続します。必要な結線は、##,##,##,##です。出力用ということで、RaspberryPi Pico 2 Wの右側のピンを使っています。ピンの割り当てはご都合に合わせて変更可能です。
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
フォントが入手できた場合、テストを描画することが可能になります。<br>
以下はテキストの描画
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

### ご参考
`https://web.archive.org/`　には2022年7月のレポジトリがアーカイブされて参照できました。公開当時のリポジトリに使用許諾は明記されていませんでした。Publicリポジトリを閉鎖されたことを考えると使うのは避けた方がよいのかもしれません。<br>
下記の6x8フォントをPython版にポーティングするか。。<br>
https://github.com/idispatch/raster-fonts/blob/master/font-6x8.c
