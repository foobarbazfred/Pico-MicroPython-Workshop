#PWMによるサーボ制御

サーボは以下のパルスでホーンの回転角度が決まります。PWMを使うことで、サーボを簡単に制御できます。サーボのホーンの角度で、疑似的にアナログ値を表現することができます。
```
from machine import Pin
from machine import PWM
servo = PWM(Pin(17), freq=50)
```
ホーンの角度はdutyによって変えることができます
```
servo.duty(40)
servo.duty(115)
servo.duty(77)
```
参考URL<br>
https://micropython-docs-ja.readthedocs.io/ja/latest/esp8266/tutorial/pwm.html#control-a-hobby-servo
