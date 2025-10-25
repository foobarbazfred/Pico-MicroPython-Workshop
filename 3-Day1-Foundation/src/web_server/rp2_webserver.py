#
#
# WebServer sample by Raspberry Pi Pico 2 W
# v0.01 (2025/10/25)
#
#
#

import machine
import rp2
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 1)]
pins += [machine.Pin(i, machine.Pin.OUT) for i in (2, 3)]

HTML_TEMPLATE = """<!DOCTYPE html>
<html>
    <head> <title>RP2350 WebServer</title> </head>
    <body> 
        <h1>RP2350 Pins</h1>
        <table border="1"> 
             <tr><th>Pin</th><th>Value</th><th>Control</th></tr>
              __TABLE_ROWS__ 
        </table>
        <h1>LED</h1>
        <table border="1"> 
              <tr><th>Device</th><th>Value</th><th>Control</th></tr> 
              <tr><td>LED0</td><td>__LED_STATUS__</td><td>__LED_CONTROL__</td></tr>
        </table>
        <h1>BUTTON</h1>
        <table border="1"> 
             <tr><th>Device</th><th>Value</th></tr> 
             <tr><td>PB0</td><td>__PB0_STATUS__</td></tr>
        </table>
        <h1>STATUS</h1>
           __UPDATE_URL__
    </body>
</html>
"""

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
    led_status = str(machine.Pin.board.LED.value())
    led_control = "<a href='/control?led0=toggle'>TOGGLE</a>"
    html = html.replace('__LED_CONTROL__', led_control)
    html = html.replace('__LED_STATUS__', led_status)
    pb0_status = str(rp2.bootsel_button())
    html = html.replace('__PB0_STATUS__', pb0_status)
    html = html.replace('__UPDATE_URL__', "<a href='/status'>UPDATE STATUS</a>")
    return html

def control(params):
    if 'led0' in params:  # 'led0=toggle'
        machine.Pin.board.LED.toggle()
    elif 'GPIO' in params:  # 'GPIO2=toggle/GPIO3=toggle'
        gpio_name = params.split('=')[0]
        for pin in pins:
             if gpio_name in str(pin):
                 pin.toggle()


import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

led_status = 'unkown'
while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    # read until CRLF
    request = ''
    while True:
        line = cl_file.readline()
        #print(line)
        if 'GET' in line:
           if 'status' in line:
                request = ('status')
           elif 'control' in line and '?' in line:
                # format of line....   b'GET /control?led0=toggle HTTP/1.1\r\n'
                target=line.decode().split(' ')[1].split('?')[1]
                request = ('control', target)
        if not line or line == b'\r\n':
            break

    response = ''
    if request == '' or  'status' in request:
        pass
    elif 'control' in request:
        control_params = request[1]
        print('control....', control_params)
        control(control_params)

    html = make_rp2_board_status_html()
    response = html

    cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
    cl.send(response)
    cl.close()
    print('close connection')

#
#
#





# request sample
#
#  b'GET /control?led0=toggle HTTP/1.1\r\n'
#  b'Host: 192.168.10.123\r\n'
#  b'Connection: keep-alive\r\n'
#  b'Upgrade-Insecure-Requests: 1\r\n'
#  b'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36\r\n'
#  b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7\r\n'
#  b'Referer: http://192.168.10.123/control?led0=toggle\r\n'
#  b'Accept-Encoding: gzip, deflate\r\n'
#  b'Accept-Language: ja,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6\r\n'
#  b'\r\n'
#