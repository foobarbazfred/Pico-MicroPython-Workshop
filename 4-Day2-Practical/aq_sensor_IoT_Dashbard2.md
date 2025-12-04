# 空気質収集とIoTダッシュボード表示(その２）

IoT ダッシュボードの作成例として、Raspberry Pi 上でNode-REDを稼働させ、Node-REDのMQTT Client ノードと、グラフ描画ノードを用いることで手軽にIoT ダッシュボードを実現することができます。

MQTT BrokerにPublishされたメッセージをNode-REDを使って見える化します
Node-REDにはグラフ化機能がありそれらを使うことで簡単にダッシュボードを作ることができます。

Node-REDを用いたIoT Dashboard<br>
<img src="assets/IAQ_sensor_Dashboard.png" width=400><br>
Node-REDのフロー<br>
<img src="assets/Node-RED_flow.png" width=700><br>
<img src="assets/Node-RED_change_node.png" width=400><br>
<img src="assets/Node-RED_gauge_node.png" width=400><br>
<img src="assets/Node-RED_mqtt_node.png" width=400><br>
<img src="assets/Node-RED_mqtt_setting.png" width=400><br>
