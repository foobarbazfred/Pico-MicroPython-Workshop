# REPLを活用した試作

  - Pythonはインタプリタのため対話的にプログラミングできます。ソースを打ち込んですぐに実行される仕組みは、Read-Eval-Print-Loop(REPL)と呼ばれます。REPLを活用してテストファーストで部品から組み上げましょう（部分から全体へ）
    - 仕様書を見ないと使い方が分からないセンサを使う場合、REPLで試行錯誤しながら制御プログラムを書く方法が効率的です
    - C言語等、コンパイル型言語の場合、特定の関数だけ抜き出して実行することはできませんが、Pythonであればテストしたい関数名をREPLから入力することで直接実行できます
   
## 対話的プログラミングの事例
もっとも簡素なTeraTermによる対話例を示します
マイコンブート時はグリーティングメッセージとバージョンが表示されます。
```
MicroPython v1.29.0 on 2026-08-24; Raspberry Pi Pico 2 W with RP2350
Type "help()" for more information.
>>>
```
画面内に、`>>>` と出ていますが、これは入力待ちを表しています。
help()と出ているので`help()`と打ってみます。
```
Welcome to MicroPython!
For online docs please visit http://docs.micropython.org/
For access to the hardware use the 'machine' module.  RP2 specific commands
are in the 'rp2' module.
　　　　　　　　　　＊中略＊
For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')
```
すぐに使えるモジュールを知りたい場合、`help('modules')`と打ち込みます。
```
>>> help('modules')
__main__          asyncio/__init__  hashlib           rp2
_asyncio          asyncio/core      heapq             select
_boot             asyncio/event     io                socket
_boot_fat         asyncio/funcs     json              ssl
_onewire          asyncio/lock      lwip              struct
_rp2              asyncio/stream    machine           sys
_thread           binascii          math              time
_webrepl          bluetooth         micropython       tls
aioble/__init__   builtins          mip/__init__      uasyncio
aioble/central    cmath             neopixel          uctypes
aioble/client     collections       network           urequests
aioble/core       cryptolib         ntptime           vfs
aioble/device     deflate           onewire           webrepl
aioble/l2cap      dht               os                webrepl_setup
aioble/peripheral ds18x20           platform          websocket
aioble/security   errno             random
aioble/server     framebuf          re
array             gc                requests/__init__
Plus any modules on the filesystem
```
Raspberry Pi Pico 2W用にビルドされたMicroPythonファームには上記モジュールがすでに入って配布されていることが分かります。
上記モジュール類はimport文によりMicroPython実行環境に取り込むことで利用可能になります。
組み込み用にマイコンごとにカスタマイズされているモジュールがmachineモジュールです。仕様書を見てもいいのですが、ざっと知りたい場合、`import machine`でモジュールを取り込んでから、`dir(machine)`と打つと内部シンボルが表示されますので、どのような機能が提供されているのか把握できます。
```
>>> import machine
>>> dir(machine)
['__class__', '__name__', 'ADC', 'I2C', 'I2CTarget', 'I2S', 'PWM', 'PWRON_RESET', 'Pin', 'RTC', 'SPI', 'Signal', 'SoftI2C', 'SoftSPI', 'Timer', 'UART', 'USBDevice', 'WDT', 'WDT_RESET', '__dict__', 'bitstream', 'bootloader', 'deepsleep', 'dht_readinto', 'disable_irq', 'enable_irq', 'freq', 'idle', 'lightsleep', 'mem16', 'mem32', 'mem8', 'mem_backup', 'reset', 'reset_cause', 'soft_reset', 'time_pulse_us', 'unique_id']
```
出力結果を見ると、machineモジュール内に、I2C,SPI,UART,Pin,ADC等、ハードウエア制御用のクラスが格納されていることが分かります。
REPLでは入力した文や式は即時実行されます。以下は変数ｘと変数yに文字列を入力してprint関数で出力する例です。
```
>>> x = 'hello'
>>> print(x)
hello
>>> y='good bye'
>>> print(x + ',' + y)
hello,good bye
>>> print(x + ', ' + y)
hello, good bye
```
for文も直接入力で実行できます。
```
>>> for x in range(10):
...     print(x)
...
...
...
0
1
2
3
4
5
6
7
8
9
```
REPLで関数を定義することもできます。
```
>>> def test(message):
...     print('your message is ' + message)
...
...
...
>>> test('hello!!')
your message is hello!!
```

## 対話的プログラミングの長所と短所

対話的プログラミング（REPL）は、短いコードをその場で実行してすぐ結果を確認できるため、**ボトムアップ開発**と非常に相性が良い手法です。特にハードウェアや外部センサを扱う場面では、仕様書やデータシートを読み込むだけでは分かりにくい挙動も、実際に値を読み書きしながら試行錯誤して理解を深められます。

### 長所

* **試行錯誤のスピードが速い:** ビルドや全体実行の手間を省き、1行〜数行単位で挙動を確かめながら進められます。
* **未知の機器・APIを探索しやすい:** センサの初期化手順や返り値の形式、通信のタイミングなどを実機で確かめながら理解できます。

### 短所・注意点

* **設計が散らかりやすい（ボトムアップの弱点）:** 思いついた順や局所的な確認から積み上げていくため、処理の重複や関数・モジュール分割の甘さが出やすくなります。動いたあとに全体を見直し、整理・リファクタリングする工程が欠かせません。
* **実行状態（ステート）が残り続ける:** REPLでは直前までに定義した変数、インポートしたモジュール、ハードウェアの設定状態が保持され続けます。「REPLでは動いたのに、ファイルに保存してリセットしたら動かなかった（変数の定義漏れや初期化忘れ）」という落とし穴に注意が必要です。
* **コードがファイルとして残らない:** 対話的に入力したコードはそのままではプログラムファイルにならないため、うまく動いた手順はエディタ側のコードへ反映・保存する習慣が必要です。

全体像を先に固めてから作るトップダウン開発（コンパイル型言語などで構造や `main()` などを整えてから組み立てるアプローチ）と比べ、ボトムアップ開発は「まず動かして確かめる」強みがある反面、**定期的な構造の見直しと整理（リファクタリング）**が必要になります。

（最後の長所と短所は自分が下書きを書いてGeminiに清書してもらいました）
