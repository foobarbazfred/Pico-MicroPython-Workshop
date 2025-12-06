import machine, rp2, socket

# --- LCD 初期化 ---
from machine import I2C
from I2C_LCD import I2CLcd
LCD_ADDR = 0x27

i2c = I2C(0)
lcd = I2CLcd(i2c, LCD_ADDR, 2, 16)

# --- 超音波センサ 設定 ---
TRIG = machine.Pin(14, machine.Pin.OUT)
ECHO = machine.Pin(15, machine.Pin.IN)

def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    while not ECHO.value():
        pass
    time1 = time.ticks_us()
    while ECHO.value():
        pass
    time2 = time.ticks_us()
    during = time.ticks_diff(time2, time1)
    return during * 340 / 2 / 10000

# --- GPIO 設定 ---
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 1)]
pins += [machine.Pin(i, machine.Pin.OUT) for i in (2, 3)]

# --- サーボ設定 (例: GPIO17 に接続) ---
servo_pin = machine.Pin(17)
servo_pwm = machine.PWM(servo_pin)
servo_pwm.freq(50)  # サーボは通常 50Hz

# サーボ角度制御関数
def set_servo_angle(angle):
    # 0°～180°を duty_u16 に変換 (例: 0.5ms～2.5ms パルス幅)
    min_duty = 1638   # 約0.5ms
    max_duty = 8192   # 約2.5ms
    duty = int(min_duty + (max_duty - min_duty) * angle / 180)
    servo_pwm.duty_u16(duty)

current_angle = 90
set_servo_angle(current_angle)

# --- HTML テンプレート ---
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head><title>RP2350 WebServer</title></head>
<body>
    <h1>RP2350 Pins</h1>
    <table border="1">__TABLE_ROWS__</table>
    <h1>LED</h1>
    <table border="1">
        <tr><td>LED0</td><td>__LED_STATUS__</td><td>__LED_CONTROL__</td></tr>
    </table>
    <h1>BUTTON</h1>
    <table border="1">
        <tr><td>PB0</td><td>__PB0_STATUS__</td></tr>
    </table>
    <h1>Servo Motor</h1>
    <table border="1">
        <tr><td>Servo0</td><td>__SERVO_STATUS__</td>
            <td>
              <a href='/control?servo=0'>0 [deg]</a> |
              <a href='/control?servo=45'>45 [deg]</a> |
              <a href='/control?servo=90'>90 [deg]</a> |
              <a href='/control?servo=135'>135 [deg]</a> |
              <a href='/control?servo=180'>180 [deg]</a>
            </td>
        </tr>
    </table>
    <h1>STATUS</h1>
    __UPDATE_URL__
</body>
</html>
"""

# --- HTML生成関数 ---
def make_rp2_board_status_html():
    rows = ''
    for pin in pins:
        if 'mode=OUT' in str(pin):
            gpio_name = str(pin).split('(')[1].split(',')[0]
            control = f"<a href='/control?{gpio_name}=toggle'>TOGGLE</a>"
        else:
            control = 'xxx'
        rows += f'<tr><td>{str(pin)}</td><td>{pin.value()}</td><td>{control}</td></tr>'
    html = HTML_TEMPLATE.replace('__TABLE_ROWS__', rows)
    html = html.replace('__LED_STATUS__', str(machine.Pin.board.LED.value()))
    html = html.replace('__LED_CONTROL__', "<a href='/control?led0=toggle'>TOGGLE</a>")
    html = html.replace('__PB0_STATUS__', str(rp2.bootsel_button()))
    html = html.replace('__SERVO_STATUS__', str(current_angle) + " deg")
    html = html.replace('__UPDATE_URL__', "<a href='/status'>UPDATE STATUS</a>")
    return html

# --- 制御関数 ---
def control(params):
    global current_angle
    if 'led0' in params:
        machine.Pin.board.LED.toggle()
    elif 'GPIO' in params:
        gpio_name = params.split('=')[0]
        for pin in pins:
            if gpio_name in str(pin):
                pin.toggle()
    elif 'servo' in params:
        angle = int(params.split('=')[1])
        set_servo_angle(angle)
        current_angle = angle

# --- ソケットサーバー ---
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

while True:
    lcd.clear()
    dis = distance()
    lcd.putstr("{:.2f} m".format(dis))
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    request = ''
    while True:
        line = cl_file.readline()
        if 'GET' in line:
            if 'status' in line:
                request = ('status')
            elif 'control' in line and '?' in line:
                target = line.decode().split(' ')[1].split('?')[1]
                request = ('control', target)
        if not line or line == b'\r\n':
            break

    if request != '' and 'control' in request:
        control(request[1])

    html = make_rp2_board_status_html()
    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(html)
    cl.close()
    print('close connection')
