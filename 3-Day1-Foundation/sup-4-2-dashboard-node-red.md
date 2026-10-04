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
