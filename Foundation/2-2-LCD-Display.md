# LCD Displayの利用

LCD Displayは16x2が表示可能、コントローラはPCF8574T (PCF8574AT)が使われています。I2Cで接続され、デバイスアドレスは0x27です。
マイコンとの接続は、5V,GNDに加え、I2Cのクロック、データバスを接続します。




The serial-to-parallel IC chip used in this module is PCF8574T (PCF8574AT), and its default I2C address is 0x27(0x3F).
