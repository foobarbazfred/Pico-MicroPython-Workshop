#
# mylib.py
#

#
# servo control function
#

# pulse width (ms)
DEGREE_0 = 0.5
DEGREE_180 = 2.4

PWM_FREQ_SERVO = 50  # 50Hz
MAX_VALUE = 0xffff
MAX_PULSE_WIDTH = 20 # max width : 20 ms in MAX_VALUE

def servo_rotate_horn(servo, degree):
    target_pulse_width = degree / 180 * (DEGREE_180 - DEGREE_0) + DEGREE_0
    servo.freq(PWM_FREQ_SERVO)  
    servo.duty_u16(int(target_pulse_width /MAX_PULSE_WIDTH * MAX_VALUE))

