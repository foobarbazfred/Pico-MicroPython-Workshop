# マイコンでセンサを制御する

### センサとは？
センサとは、外界の物理的、化学的な現象を電気信号に変換し、マイコン等で計測可能にする装置です。

### どんなセンサがある？

- 温度センサ
  -  温度を測るセンサです。接触型、非接触型があります   
- 圧力、ひずみセンサ
  - 重さや圧力、物体のひずみを測るセンサです 
- 音、振動センサ
  - 音や振動を測るセンサです 
- 磁気センサ
  - 磁気(磁力)を測るセンサです（方位を観察したり、回転を観察） 
- 空気質、ガスセンサ
  - 部屋の温湿度、CO2、窒素酸化物の濃度を測るセンサ 
- 動き,動きセンサ
  -  XYZ軸方向の加速度や回転(ヨーローピッチ)を測るセンサです。GPSにより現在位置を測ることができます
- 距離、接触センサ
  - 対象物までの距離や接触しているかを測るセンサ 
- 画像センサ
  - 画像を取得するセンサ(カメラ) 
- 生体センサ
  - 心拍数や血中濃度、心電位、脳波等を測るセンサ 
- その他



### 使い方は？
センサとマイコンとの接続方法として、アナログ出力による接続、デジタル出力による接続に分かれます。アナログ出力としては、センサが出力する電圧変化や抵抗変化をマイコンで読み取ります。
デジタル出力としては、Serial, I2C, SPI, I2S等が用いられます。マイコンの周辺I/Oを使ってセンサと接続し、データを読み取ります。

アナログ出力のセンサは小型で安価ですが、信号の扱いが難しい問題があります。特に、微弱な電圧で出力された電圧を計測可能な電圧までオペアンプ等を使って増幅する必要があり、追加回路が必要な場合が多いです。また出力特性に応じて、変換関数が必要になる場合があります。

手軽に扱えるのはデジタル出力のセンサです。まずはデジタル出力から使ってみることをお勧めします。

デジタル出力の場合、マイコンと直結すれば制御可能ですが、Serial , I2C , SPI の接続IFに応じてプログラムが必要です。BME260,BME680等、有名なセンサは制御用モジュール(ドライバと呼ばれます)が公開されています。センサ名で、例えば、　github  micropython driver BME280  のキーワードで検索すれば、ドライバを見つけられます。Copilotに質問しても回答が得られます。以下はプロンプト例
```
Python版BME280用のドライバはGitHubにありますか？
```


### I2C接続、SPI接続できるセンサはどのようなものがある？

[秋月；センサ+I2Cで検索](https://akizukidenshi.com/catalog/goods/search.aspx?keyword=&ct=0605&goods=&number=&name=&min_price=&max_price=&yy_min_releasedt=&mm_min_releasedt=&dd_min_releasedt=&yy_max_releasedt=&mm_max_releasedt=&dd_max_releasedt=&last_sdt=&gt=&goods_specification=%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%95%E3%82%A7%E3%82%A4%E3%82%B9%EF%BC%9AI2C&seq=gn&maker_name=&search=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B&variation=)<br>
[秋月；センサ+SPIで検索](https://akizukidenshi.com/catalog/goods/search.aspx?keyword=&ct=0605&goods=&number=&name=&min_price=&max_price=&yy_min_releasedt=&mm_min_releasedt=&dd_min_releasedt=&yy_max_releasedt=&mm_max_releasedt=&dd_max_releasedt=&last_sdt=&gt=&goods_specification=%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%95%E3%82%A7%E3%82%A4%E3%82%B9%EF%BC%9ASPI&seq=gn&maker_name=&search=%E6%A4%9C%E7%B4%A2%E3%81%99%E3%82%8B&variation=)<br>
[Adafruit社；センサ一覧](https://www.adafruit.com/category/35?srsltid=AfmBOopckPgLodnKvVW4jFYxSvkfkuLSZ2BhRSSDlvlPjNsN7y5mui_a)

### センサ参考文献
センサ活用を詳しく解説した本<br>
実用センサ&回路大事典<br>
https://cc.cqpub.co.jp/lib/system/doclib_item/1376<br>
Interface 2025年 8月号　IoTセンサ図鑑[2025年版]<br>
https://interface.cqpub.co.jp/magazine/202508/<br>
RPiでセンサを使う方法(サンプルコード、活用事例)<br>
