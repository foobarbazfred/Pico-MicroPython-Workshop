# 空気質収集とIoTダッシュボード表示(その２）

IoT ダッシュボードの作成例として、Raspberry Pi 上でNode-REDを稼働させ、Node-REDのMQTT Client ノードと、グラフ描画ノードを用いることで手軽にIoT ダッシュボードを実現することができます。

MQTT BrokerにPublishされたメッセージをNode-REDを使って見える化します
Node-REDにはグラフ化機能がありそれらを使うことで簡単にダッシュボードを作ることができます。

Node-REDを用いたIoT Dashboard<br>
<img src="assets/IAQ_sensor_Dashboard.png" width=400><br>
Node-REDのフロー<br>
<img src="assets/Node-RED_flow.png" width=700><br>

- MQTT メッセージの受信はMQTT INノードを用います。<br>
MQTT INノードを使うことで、Subscribeが自動的に行われ、条件に合ったメッセージが発行されると、MQTT INノードにデータが送信されます<br>
<img src="assets/Node-RED_mqtt_node.png" width=400><br>
<img src="assets/Node-RED_mqtt_setting.png" width=400><br>

送信されたデータは、JSON形式で、温度、湿度、CO2濃度がまとまっていますので、Changeノードを使って、温度だけを取り出します。<br>
<img src="assets/Node-RED_change_node.png" width=400><br>
msg.payloadに温度情報を入れて、ゲージノードにメッセージを流します。ゲージノードは上流(Changeノード）から送られてきたメッセージを参照して、ゲージの表示を更新します<br>
<img src="assets/Node-RED_gauge_node.png" width=400><br>
