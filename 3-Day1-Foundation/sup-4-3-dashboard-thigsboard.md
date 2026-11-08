# ThingsBoardによるIoT プラットフォーム実装
ThingsBoardはクラウド版を使う場合、基本有償ですが、CommunityEdition版(CE版)が提供されており、サーバを調達して、自分でThingsBoardサービスを立ち上げることができます

- [GitHub](https://github.com/thingsboard/thingsboard)
- [ThingsBoard CE版Installガイド](https://thingsboard.io/docs/user-guide/install/installation-options/)


### Dockerを使ったThingsBoard構築例

Docker composeによるThingsBoardサービスの立ち上げ例を示します。
1. データ永続化のため、コンテナから外部ストレージとして使うディレクトリを作成します
```
mkdir -p ~/.mytb-data && sudo chown -R 799:799 ~/.mytb-data
mkdir -p ~/.mytb-logs && sudo chown -R 799:799 ~/.mytb-logs
```
UID:GIDを799:799にしているのは、Dockerコンテナ内でThingsBoardのプロセスが799:799で動作しており、ファイルR/W時に権限違反を起こさないため

2. Docker compose用のymlファイルを作成します。<br>
file:docker-compose.yml (ミニマム版)
```
services:
  mytb:
    restart: always
    image: "thingsboard/tb-postgres"
    ports:
      - "8080:9090"
      - "1883:1883"
      - "7070:7070"
      - "5683-5688:5683-5688/udp"
    environment:
      TB_QUEUE_TYPE: in-memory
    volumes:
      - ~/.mytb-data:/data
      - ~/.mytb-logs:/var/log/thingsboard
```
3. イメージをビルドしてコンテナを起動します
```
docker compose up -d
```
4. コンテナが起動されますので、ブラウザからThingsBoardのログイン画面にアクセスします
```
http://<サーバのIP>:8080/
```
サービス起動後のログインIDは以下を参照してください
[start the platform](https://thingsboard.io/docs/installation/docker/#step-3-start-the-platform)
