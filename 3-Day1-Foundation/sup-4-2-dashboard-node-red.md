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
<img width="566" height="552" alt="image" src="https://github.com/user-attachments/assets/f5142920-43bf-44e8-ae0d-867797605021" /><br>
パレットにdashboard用Nodeが追加されます<br>
<img width="275" height="629" alt="image" src="https://github.com/user-attachments/assets/14641cae-3710-45d1-98f2-b842306005f1" />

### Node-REDによるプログラミング
1. まず、ダッシュボードメニューより、タブとグループを追加します（表示するための場所確保です）
2. 次に、MQTTブローカに接続して受信するため、MQTT NodeをDrag＆Dropします。またGUI表示のためのWidgetである、Gauge Node、Graph NodeをDrag&Dropします。
3. MQTTノードで受信されるデータはJSON形式です。JSON形式データから測定データを取り出したいので、changeノードで計測値だけを取り出します。
4. MQTT Node、Change Node、Gauge Node、Graph Nodeをwireで接続してデータが流れるようにします。
5. プログラムが完了すると、右上のデプロイをクリックします。これによりIoT Dashboardが利用可能となります。画面に接続するには、右矢印をクリックします。ブラウザが起動されます。

<img width="810" height="486" alt="image" src="https://github.com/user-attachments/assets/1a4f3965-3c73-48da-b449-34151fda8773" />
<img width="562" height="406" alt="image" src="https://github.com/user-attachments/assets/b55ef745-420f-48db-b3b7-9fdebb306a8a" />
<img width="611" height="509" alt="image" src="https://github.com/user-attachments/assets/5b55349e-5b55-4c3a-b5ba-e165a9f4b2cc" />
<img width="963" height="634" alt="image" src="https://github.com/user-attachments/assets/94a0273a-6422-4996-82ff-99b4b12700b8" />
<img width="1007" height="605" alt="image" src="https://github.com/user-attachments/assets/36e03628-c5a3-4dab-8927-2683febf1893" />

### 動作確認
正しく動作すると以下のように、1秒に一回表示が更新されます。
<img width="1340" height="904" alt="image" src="https://github.com/user-attachments/assets/fae363ad-925d-4e97-afc4-5657f9eb7563" />
