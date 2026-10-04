# GPSの利用

GPSを用いることで、正確な位置情報や時刻の取得が可能になります。USB接続のGPSユニットとUART接続のGPSユニットがあります。マイコンとの接続を考えると、UART接続のGPSユニットを選択するのが良いと思います。GPUユニットを制御するためのコマンドが提供されており、出力情報の選択、UART転送レートの変更等がコマンドを用いて行えます。どのGPSユニットも、マイコン側から細かい制御をせずとも電源投入するとGPSは自動的に衛星からの電波を受信して得られた情報をUARTを使ってマイコンに送信してきます。多くの衛星をキャッチした結果、GPSユニットから送られている受信データが多すぎる場合、GPSユニットからの送信情報を減らす設定を行います。

GPSユニットの仕様
- 製品名：GT-502MGG-N
- みちびき2機(194/195)対応
- UART接続
  - 9600bps(RX,TX)
  - 1秒単位の同期信号付き
### 配線図
<img src="assets/Schematics_GPS.png" width=700>

ソース一式
[gps_gt-502.py](src/gps_gt-502.py)

### 参考資料
- 秋月GPSページ
  - https://akizukidenshi.com/catalog/c/csatellit/
  - 商品説明に「シリアル出力タイプ」と書かれているGPUユニットは、UARTで接続可能です
- GPS(GT-502MGG) Specification
  - https://akizukidenshi.com/goodsaffix/GT-502MGG.pdf

