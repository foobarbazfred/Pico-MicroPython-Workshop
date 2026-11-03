# C言語とMicroPythonの性能差
MicroPythonとC言語との間でどれぐらい性能の差があるのかを単純なGPIOのL/Hを繰り返すプログラムで比較

コンパイル型言語のC言語とインタプリタ型言語のMicroPython を単純に比べるのはどうかとは思いつつ、性能差を把握するため比較

### 処理時間と考察

|   |C言語|MP言語:関数化	| MP言語:関数化+native最適化	| MP言語:関数化+viper最適化+レジスタ直接書き込み|
|---|----|----|----|----|
|パルスの周期|	34.4ns (29MHz)	|192.3KHz / 5.200us	|250.0KHz(1.3倍)	|694.4KHz(3.6倍)|
|処理時間比	|151倍|1倍|	1.3倍|	3.6倍|
|処理時間比	|1倍|0.007倍(1/151)|	0.009倍(1/116)| 0.02倍(1/50)|

- クロックは150MHzに設定

### C言語ソース
```
#include "pico/stdlib.h"
#include "hardware/clocks.h"  
#define OUT_PIN  1   // GPIO:1  for output

int main() {

    // set systemclock to 150MHz
    set_sys_clock_khz(150000, true);

    // setup GPIO for output
    gpio_init(OUT_PIN);
    gpio_set_dir(OUT_PIN, GPIO_OUT);

    while (true) {
       gpio_put(OUT_PIN, 1);   // H
       gpio_put(OUT_PIN, 0);   // L
    }
}
// 34.4ns (29MHz)
```


### MicroPython言語 ループ処理関数化＋Pin操作インライン展開+viper最適化
```
import machine
from machine import Pin

#SIO_BASE_REG = 0xd0000000
#SIO_GPIO_OUT_SET_REG_OFFSET = 0x18
#SIO_GPIO_OUT_CLR_REG_OFFSET = 0x20

@micropython.viper
def _gp1_set_clr():
    while True:
        # 0xd0000018 : SIO_GPIO_OUT_SET_REG
        ptr32(0xd0000018)[0] = 0x00_02  # 0x00_02 means gpio:1
        # 0xd0000020 : SIO_GPIO_OUT_CLR_REG
        ptr32(0xd0000020)[0] = 0x00_02  # 0x00_02 means gpio:1

machine.freq(150_000_000)
print(machine.freq())   # 150_000_000
pin1 = Pin(1, Pin.OUT)
_gp1_set_clr()

# 694.4KHz (1.440us)
```
