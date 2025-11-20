### どうやってプログラミングするか？
1. ターミナルから直接入力
2. PC上のエディタでソースコードを作成、MicroPythonにCopy&Pasteで貼り付ける
3. PC上のIDE（統合開発環境）でソースコードを作成、MicroPythonに転送する
4. PC上のディタでソースコードを作成、メンテナンス用ツール(CLIコマンド)を使って、MicroPythonに転送する

### MicroPythonの起動シーケンス
- 電源が投入されると、MicroPythonはファイルシステム上のboot.pyを読み込んで実行します。boot.pyの実行が終わると、main.pyを読み込んで実行します。全ての実行が終わると、入力待ちになります。
- boot.pyは、Wi-Fi設定等、環境整備用のプログラムを入れておくと良いと思います。皆様のPicoにもWi-Fi設定と時刻同期、uPyShのimportが行われています。
