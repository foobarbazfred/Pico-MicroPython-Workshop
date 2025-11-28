# PWMによるサーボ制御

サーボは以下のパルスでホーンの回転角度が決まります。

- サーボ制御波形の基本仕様
  - 周波数：50Hz（周期20ms）
- パルス幅（HIGH時間）：
  - 最小角度（0°） : 約0.5ms
  - 中央（90°） : 約1.5ms 
  - 最大角度（180°） : 約2.4ms 

サーボモータの結線
- 赤：5V
- 茶：GND(0V)
- 橙：制御信号(PWM)(3.3V)


PWMを使うことで、サーボを簡単に制御できます。サーボのホーンの角度で、疑似的にアナログ値を表現することができます。
```
from machine import Pin
from machine import PWM
servo = PWM(Pin(17), freq=50)
```
ホーンの角度はPWMのdutyによって変えることができます
```
MAX_VALUE = 0xffff
servo.duty_u16(int(0.5/20 * MAX_VALUE))  # angle : 0 degree
servo.duty_u16(int(1.5/20 * MAX_VALUE))  # angle : 90 degrees
servo.duty_u16(int(2.4/20 * MAX_VALUE))  # angle : 180 degrees
```
指定された角度にアームを回転させるプログラム（関数化）
```
#
# servo control function
#
from machine import Pin
from machine import PWM

# pulse width (ms)
DEGREE_0 = 0.5
DEGREE_180 = 2.4

PWM_FREQ_SERVO = 50  # 50Hz
MAX_VALUE = 0xffff
MAX_PULSE_WIDTH = 20 # max width : 20 ms in MAX_VALUE

SERVO_PIN = 17

def servo_rotate_horn(servo, degree):
    target_pulse_width = degree / 180 * (DEGREE_180 - DEGREE_0) + DEGREE_0
    servo.freq(PWM_FREQ_SERVO)  
    servo.duty_u16(int(target_pulse_width /MAX_PULSE_WIDTH * MAX_VALUE))

# test
import time
def servo_test():
    # initialize PWM for servo control
    servo = PWM(Pin(SERVO_PIN), freq=PWM_FREQ_SERVO)
    print('rotate 0 degree')
    servo_rotate_horn(servo, 0)
    time.sleep(1)
    print('rotate 45 degree')
    servo_rotate_horn(servo, 45)
    time.sleep(1)
    print('rotate 90 degree')
    servo_rotate_horn(servo, 90)
    time.sleep(1)
    print('rotate 135 degree')
    servo_rotate_horn(servo, 135)
    time.sleep(1)
    print('rotate 180 degree')
    servo_rotate_horn(servo, 180)
    time.sleep(1)
    print('rotate 90 degree')
    servo_rotate_horn(servo, 90)
    time.sleep(1)
    print('rotate 0 degree')
    servo_rotate_horn(servo, 0)

# servo_test()
```

サーボ制御関数は共通ライブラリ、mylib.pyに入れていますので以下のコードで利用できます。
```
from mylib import servo_rotate_horn
from mylib import PWM_FREQ_SERVO       # 50Hz

SERVO_PIN = 17
servo = PWM(Pin(SERVO_PIN), freq=PWM_FREQ_SERVO)
servo_rotate_horn(servo, 90)
```

可変抵抗（ボリューム）の軸の回転に連動してサーボのホーンを動かすプログラムは以下
```
from machine import Pin
from machine import ADC
from machine import PWM
from mylib import servo_rotate_horn
from mylib import PWM_FREQ_SERVO

VR_INPUT_PIN = 26
SERVO_PIN = 17

adc = ADC(Pin(VR_INPUT_PIN))     # create ADC object on ADC pin
servo = PWM(Pin(SERVO_PIN), freq=PWM_FREQ_SERVO)
while True:
    vr = adc.read_u16() 
    degree = int(180 * vr / 0xffff)
    servo_rotate_horn(servo, degree)
```
参考URL<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/esp8266/tutorial/pwm.html#control-a-hobby-servo
