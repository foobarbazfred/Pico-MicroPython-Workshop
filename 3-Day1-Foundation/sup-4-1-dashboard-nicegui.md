# NiceGUI+Python+MQTT ClientによるDashboard実装

きれいなGUI画面を作るのは大変ですが、StreamlitやNiceGUI等のモジュールを活用することで、見栄えのよいDashboardが比較的簡単に実現できます。IoT プラットフォームを契約して利用する場合基本的に有償となりますが、自作すればコストはほぼ０円です。

NiceGUI + Pythonによる自作dashboardの表示例<br>
<img width="1200" height="592" alt="image" src="https://github.com/user-attachments/assets/02c3e94c-6a0c-4b43-bfc6-7105a309ede0" />


### 自前でIoTダッシュボードを構築する (NiceGUI編)
- Streamlit, NiceGUI等を使ってIoTダッシュボードを自作
- Python+NiceGUI(Streamlit)を使ってWebServiceを開発、PCかRPi上でWevServiceを稼働させる
- NiceGUI/Streamlitの場合Widgetが用意されており、画面構築は比較的容易(VisualProgrammingよりは手間)
- 自分で実装するので自由度が高い、表示対象データの特性に最適化可能
- セキュリティ面から、インターネット上でのサービス提供は不可
- ローカルネットワーク環境からの利用に留めるべき
- IoTプロトタイプ試作の学びに適する
   - センサ→マイコン(RP2W)→MQTTブローカ→IoTダッシュボード自作(onPC/RPi)というIoTシステムの試作を通してシステム設計開発を学べる


### ソース一式

