# Node-REDのSashboard機能活用

RP2Wとセンサを接続して計測したデータを表示する方法として、Node-REDのDashBoard機能を使う方法があります

### 自力でIoTダッシュボードを構築する
- Node-RED Dashboard機能を使う
  - PCかRPi上でNode-REDを稼働させ、Dashboard機能を使ってIoT ダッシュボードを構築する
  - No Codeか、最低限のVisual Programmingでダッシュボードが構築可能
  - セキュリティ面から、サービス提供はローカルネットワーク環境のみに制限すべき(インターネット上でのサービス提供は危険)
  - リモートから参照してもらいたい時はVPN等を構築
