# NeoPixelの制御

組み込みライブラリのNeoPixelではタイミングが守れないためか正常に動作しません。freenoveが提供するNeoPixelドライバはPIOによりタイミング制御されており、正常に動くと思われます。以下に置いていますので、このライブラリを使ってください。
https://raw.githubusercontent.com/foobarbazfred/Pico-MicroPython-Workshop/refs/heads/main/Foundation/src/lib/neopixel.py
