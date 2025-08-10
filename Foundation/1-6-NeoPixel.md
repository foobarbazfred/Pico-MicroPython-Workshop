# NeoPixelの制御

組み込みライブラリのNeoPixelではタイミングが守れないためか正常に動作しません。freenoveが提供するNeoPixelドライバはPIOによりタイミング制御されており、正常に動くと思われます。以下に置いていますので、このライブラリを使ってください。
https://raw.githubusercontent.com/foobarbazfred/Pico-MicroPython-Workshop/refs/heads/main/Foundation/src/lib/neopixel.py

組み込みモジュールとの衝突を避けるため、neopixel2.py等と名前を変えてMicroPythonにインストールしてください。
上記ライブラリが正しく使えているかは以下で確認してください。
```
>>> import neopixel2
>>> dir(neopixel2)
['__class__', '__name__', 'Pin', '__dict__', '__file__', 'array', 'rp2', 'time', 'ws2812', 'myNeopixel']
```
dir(neopixel2)と入力すると、neopixel2モジュール内のシンボル一覧が表示されます。myNeopixelが含まれているとPIOを用いたfreenove版がロードされています。
