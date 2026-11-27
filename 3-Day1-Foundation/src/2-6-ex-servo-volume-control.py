#
# file: servo_volume_control.py
# 機能：可変抵抗（ボリューム）のアナログ入力値をAD変換でデジタル化、得られた値をサーボの回転角度に変換して
#      サーボのホーンを回転させる
#
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
