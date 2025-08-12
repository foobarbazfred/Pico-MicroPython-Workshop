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
- 橙：制御信号(PWM)


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

MAX_VALUE = 0xffff
MAX_PULSE_WIDTH = 20 # max width : 20 ms in MAX_VALUE

def servo_rotate_arm(servo, degree):
    target_pulse_width = degree / 180 * (DEGREE_180 - DEGREE_0) + DEGREE_0
    servo.duty_u16(int(target_pulse /MAX_PULSE_WIDTH * MAX_VALUE))

# test
import time
def servo_test():
    servo = PWM(Pin(17), freq=50)
    print('rotate 0 degree')
    servo_rotate_arm(servo, 0)
    time.sleep(1)
    print('rotate 45 degree')
    servo_rotate_arm(servo, 45)
    time.sleep(1)
    print('rotate 90 degree')
    servo_rotate_arm(servo, 90)
    time.sleep(1)
    print('rotate 135 degree')
    servo_rotate_arm(servo, 135)
    time.sleep(1)
    print('rotate 180 degree')
    servo_rotate_arm(servo, 180)
    time.sleep(1)
    print('rotate 90 degree')
    servo_rotate_arm(servo, 90)
    time.sleep(1)
    print('rotate 0 degree')
    servo_rotate_arm(servo, 0)

# servo_test()
```


可変抵抗（ボリューム）の軸の回転に連動してサーボのホーンを動かすプログラムは以下
```
   <ここにコード>
```
参考URL<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/esp8266/tutorial/pwm.html#control-a-hobby-servo
