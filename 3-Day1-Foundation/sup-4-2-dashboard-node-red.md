# Node-REDのSashboard機能活用

RP2Wとセンサを接続して計測したデータを表示する方法として、Node-REDのDashBoard機能を使う方法があります

### 自力でIoTダッシュボードを構築する
- Node-RED Dashboard機能を使う
  - PCかRPi上でNode-REDを稼働させ、Dashboard機能を使ってIoT ダッシュボードを構築する
  - No Codeか、最低限のVisual Programmingでダッシュボードが構築可能
  - セキュリティ面から、サービス提供はローカルネットワーク環境のみに制限すべき(インターネット上でのサービス提供は危険)
  - リモートから参照してもらいたい時はVPN等を構築

### Node-REDの準備
#### Node-RED dashboardを追加します
<img width="1132" height="1105" alt="image" src="https://github.com/user-attachments/assets/f5142920-43bf-44e8-ae0d-867797605021" />
パレットにdashboard用Nodeが追加されます
<img width="275" height="629" alt="image" src="https://github.com/user-attachments/assets/14641cae-3710-45d1-98f2-b842306005f1" />

### Node-REDによるプログラミング
1.  まず、ダッシュボードメニューより、タブとグループを追加します（表示するための場所確保です）<br><img width="1004" height="602" alt="image" src="https://github.com/user-attachments/assets/97e322de-1c31-42d4-b821-27b73cbc019f" />
1. 次に、MQTTブローカに接続して受信するため、MQTTノードをDrag＆Drop、表示用のNode、GaugeNode、GraphNodeをDrag&Drop
2. MQTTノードで受信されるデータはJSON形式で、以下の値となっているため、changeノードで計測値だけを取り出します。
3. プログラムが完了すると、右上のデプロイをクリックします。これによりIoT Dashboardが利用可能となります。画面に接続するには、右矢印をクリックします。ブラウザが起動されます。

<img width="562" height="406" alt="image" src="https://github.com/user-attachments/assets/b55ef745-420f-48db-b3b7-9fdebb306a8a" />
<img width="611" height="509" alt="image" src="https://github.com/user-attachments/assets/5b55349e-5b55-4c3a-b5ba-e165a9f4b2cc" />
<img width="963" height="634" alt="image" src="https://github.com/user-attachments/assets/94a0273a-6422-4996-82ff-99b4b12700b8" />



<img width="1006" height="605" alt="image" src="https://github.com/user-attachments/assets/e8cf2779-dfa8-4e72-99a7-2cf921621a08" />



### 動作確認
正しく動作すると以下のように、1秒に一回表示が更新されます。
<img width="1340" height="904" alt="image" src="https://github.com/user-attachments/assets/fae363ad-925d-4e97-afc4-5657f9eb7563" />
