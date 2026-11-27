#
# file: servo_rotate_PWM.py
# 概要：PWMによるサーボ制御サンプルコード
#      アームの角度を0度から180度まで回転させる

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
