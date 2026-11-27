#
# file: servo_sample_w_lib.py
# 機能：mylib内で定義された servo制御関数、servo_rotate_horn()を使ったサンプルコード
#
from mylib import servo_rotate_horn
from mylib import PWM_FREQ_SERVO       # 50Hz

SERVO_PIN = 17
servo = PWM(Pin(SERVO_PIN), freq=PWM_FREQ_SERVO)
servo_rotate_horn(servo, 90)
