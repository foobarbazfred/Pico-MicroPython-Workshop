MicroPython firmを焼く

https://micropython.org/download/RPI_PICO2_W/

downloadしたファイルをDrag&DropでPico2Wのドライブにコピー<br>
RPI_PICO2_W-20250809-v1.26.0.uf2　等

一度リセットをかけて、TeraTermやThonnyで接続、下記のような起動メッセージが表示される
```
MPY: soft reboot
MicroPython v1.26.0 on 2025-08-09; Raspberry Pi Pico 2 W with RP2350
Type "help()" for more information.
```
REPL環境でhelp('modules')を実行すると、組み込みモジュールが一覧表示されます。
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
