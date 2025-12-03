#-------------------------------
#
# GPS Program for GT-502GG Series
# V0.01  2024/11/29  09:00
#
# change init variable
#  timeout=10, timeout_char=100
#  + pass through 
#  + LAT/LON
#-------------------------------

from machine import UART, Pin
import micropython
import time
import _thread

import lcd

# available UART0/UART1
#
# UART0 mapps  GPIO 0/1A12/13A16/17 
# UART1 mapps  GPIO 4/5A8/9 

# debug flag
DBG = False

DEFAULT_BAUD_RATE = 9600
HIGHSPEED_BAUD_RATE = 38400

# define pass through mode (for connect GPS Application) or not
PASS_THROUGH_MODE = False

# define global variables
uart0 = None
pps_LED = None
onepps = None
mutex = None
ym_str = ''
hm_str = ''
lat_str = ''
lon_str = ''

#
# SPECIAL CHARACTER DEF
# available only ST7032 Character Table
#
DEGREE_SYMBOL = 0xDF   

#--------------------------------------------
#  main
#--------------------------------------------

def main():

    GPS_setup()
    GPS_message_loop()

def GPS_setup():

    global uart0
    global onepps
    global mutex
    global ym_str
    global hm_str
    global lat_str
    global lon_str
    global pps_LED

    # setup UART
    uart0 = UART(0, baudrate=DEFAULT_BAUD_RATE)
    uart0.init(baudrate=DEFAULT_BAUD_RATE, tx=Pin(16), rx=Pin(17), rxbuf=2048, timeout=10, timeout_char=100)

    # setup GPIO
    onepps = Pin(20, Pin.IN)
    pps_LED = Pin(21, Pin.OUT)

    # create mutex
    mutex = _thread.allocate_lock()

    ym_str = ''
    hm_str = ''
    lat_str = ''
    lon_str = ''

    onepps.irq(handler=intr_onepps, trigger=Pin.IRQ_FALLING, hard=True)

    if PASS_THROUGH_MODE:
          GPS_receive_all_messages(uart0)   # unset supress GSV,GSA
          pass
    else:                      # SYNC 
          GPS_reduce_messages(uart0)   # supress GSV,GSA

    # setup LCD
    lcd.lcd_cls(lcd.i2c)



def GPS_message_loop():

 while True:
   received_data = ''
   if uart0.any() > 0:
       try: 
            uart_data = uart0.readline()
            received_data = uart_data.decode("ascii", "ignore").strip('\r\n')
       except UnicodeError as e:
           print('decode error, so drop received_data') 
           print(uart_data) 
           continue

       if DBG:
           print('-----------------------')
           print(f'R:[{received_data}]')

       if PASS_THROUGH_MODE:
           print(received_data)

       sentence = received_data.split(',')[0]
       if sentence == '$GPZDA':
            parse_ZDA(received_data)
       elif sentence == '$GPGGA': 
            parse_GGA(received_data)
       elif sentence == '$GPGSV': 
            parse_GSV(received_data)
       elif sentence == '$GPRMC': 
            parse_RMC(received_data)
       elif sentence == '$GPVTG': 
            parse_VTG(received_data)
       elif sentence == '$GPGLL': 
            parse_GLL(received_data)
       elif sentence == '$GPGSA': 
            parse_GSA(received_data)
       elif sentence == '$GAGSA':
            pass
       elif sentence == '$GAGSV':
            pass
       elif sentence == '$GLGSA':
            pass
       elif sentence == '$GLGSV':
            pass
       elif sentence == '$GNGGA':
            parse_GGA(received_data)
       elif sentence == '$GNGLL':
            parse_GLL(received_data)
       elif sentence == '$GNRMC':
            parse_RMC(received_data)
            pass
       elif sentence == '$GNVTG':
            pass
       elif sentence == '$PMTK010':
            pass
       elif sentence == '$PMTK011':
            pass
       else:
            parse_ANY(received_data)
   else:
       time.sleep_ms(1)



#to stop interrup
#onepps.irq(handler=None)

def intr_onepps(inter):
    pps_LED.on()
    micropython.schedule(update_LCD_info, None)

#
#
#  update LCD information
#
#
_local_var_lcd_count=0
def update_LCD_info(args):

    global _local_var_lcd_count

    if not PASS_THROUGH_MODE:
        print("update lcd")

    with mutex:
       display_info = (ym_str, hm_str)

    if _local_var_lcd_count % 15 == 0:
        # display date and time
        lcd.lcd_cls(lcd.i2c)
        lcd.lcd_print(lcd.i2c, display_info[1], display_info[0])
        lcd.lcd_home(lcd.i2c)

    elif _local_var_lcd_count % 15 == 12:
        # display Lat and Lon
        lcd.lcd_cls(lcd.i2c)
        lcd.lcd_print(lcd.i2c, lat_str, lon_str)
        lcd.lcd_home(lcd.i2c)

    elif _local_var_lcd_count % 15 > 12:
        # display Lat and Lon (no need cls)
        lcd.lcd_print(lcd.i2c, lat_str, lon_str)
        lcd.lcd_home(lcd.i2c)

    else:
        # display time only
        lcd.lcd_print(lcd.i2c, display_info[1])
        lcd.lcd_home(lcd.i2c)

    _local_var_lcd_count += 1
    if _local_var_lcd_count > 1000:
       _local_var_lcd_count = 0

    pps_LED.off()


def parse_GGA(data):
    if DBG or not PASS_THROUGH_MODE:
        print(data)
    (sentence, time, lat, ns, lon, ew, _, _, _, _, _, _, _, _, _)  = data.split(',')
    if not PASS_THROUGH_MODE:
        print(f'{ns}:{lat}, {ew}:{lon}, {time}')    


# ZDA message is NMEA-0183 standard
def parse_ZDA(data):
    global ym_str
    global hm_str
    if DBG:
        print('ZDA')
        print(data,'<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<',end='')
    (sentence, time_ms, day , month, year,_,_) = data.split(',')
    hour=time_ms[0:2]
    min=time_ms[2:4]
    sec=time_ms[4:6]
    msec=time_ms.split('.')[1]

    if day != '' and month != '' and year != '' and hour != '' and  min != '' and  sec != '' and msec != '':
        pass
    else:              # must be brush up
        day = 0
        month = 0
        year =  0
        hour =  0
        min =  0
        sec =  0
        msec =  0

    # UTC->JST convert
    # convert string to int
    (year,month,day,hour,min,sec) = [x for x in map(int, (year,month,day,hour,min,sec))]

    #(local_year,local_month,local_day,local_hour,local_min,local_sec,_,_) = get_local_time(year,month,day,hour,min,sec)
    #ym_str = f'{local_year}/{local_month}/{local_day}'
    #hm_str = f'{local_hour}:{local_min}:{local_sec}.{msec}'
    #if not PASS_THROUGH_MODE:
    #    print(ym_str, hm_str)

    # make 1 sec after
    (local_year,local_month,local_day,local_hour,local_min,local_sec,_,_) = get_local_time(year,month,day,hour,min,sec,onesec_after=True)
    with mutex:
        ym_str = f'{local_year:04d}/{local_month:02d}/{local_day:02d}'
        hm_str = f'{local_hour:02d}:{local_min:02d}:{local_sec:02d}'
    if not PASS_THROUGH_MODE:
        print('next:', ym_str, hm_str)


def parse_GSV(data):
    if DBG:
        print('GSV')
        print(data)
    pass


dbg_data = None
dbg_lat = None
dbg_lon = None

def parse_RMC(data):

    global ym_str
    global hm_str

    global lat_str
    global lon_str

    global dbg_data
    global dbg_lat
    global dbg_lon



    hour = 0
    min = 0
    sec = 0
    msec = 0

    day = 0
    month = 0
    year = 0

    if not PASS_THROUGH_MODE:
        print(data)
    dbg_data = data
    data_list = data.split(',')
    if len(data_list) == 13:
         pass
    else:
         print('format error')
         return

    sentence = data_list[0]
    rmc_time = data_list[1]
    rmc_date = data_list[9]

    lat = data_list[3]
    dbg_lat = lat
    lat_ne = data_list[4]
    lon = data_list[5]
    dbg_lat = lon
    lon_ew = data_list[6]
    if not PASS_THROUGH_MODE:
        print(f'LAT:[{lat}], LON:[{lon}]')
 
    (dd,mm,ss) = dmpmf2dms(float(lat))
    lat_str = f'{lat_ne} {dd:3d}{DEGREE_SYMBOL:c}{mm:2d}\'{ss:5.2f}"'

    (dd,mm,ss) = dmpmf2dms(float(lon))
    lon_str = f'{lon_ew} {dd:3d}{DEGREE_SYMBOL:c}{mm:2d}\'{ss:5.2f}"'

    if rmc_time != '':
        hour = int(rmc_time[0:2])
        min = int(rmc_time[2:4])
        sec = int(rmc_time[4:6])
        msec = float(rmc_time[6:])

    if rmc_date != '':
        day = int(rmc_date[0:2])
        month = int(rmc_date[2:4])
        year = 2000 + int(rmc_date[4:6])

    # make 1 sec after
    (local_year,local_month,local_day,local_hour,local_min,local_sec,_,_) = get_local_time(year,month,day,hour,min,sec,onesec_after=True)
    with mutex:
        ym_str = f'{local_year:04d}/{local_month:02d}/{local_day:02d}'
        hm_str = f'{local_hour:02d}:{local_min:02d}:{local_sec:02d}'
    if not PASS_THROUGH_MODE:
        print('next:', ym_str, hm_str)
        print('next:', lat_str, lon_str)

def parse_VTG(data):
    if DBG:
        print('VTG')
        print(data)
    pass

# $GNGLL,3445.2322,N,13539.4029,E,082728.000,A,A*45
def parse_GLL(data):
    if DBG or not PASS_THROUGH_MODE:
        print(data)
    (_, lat, ns, lon, ew, time, _, _)  = data.split(',')
    if not PASS_THROUGH_MODE:
        print(f'{ns}:{lat}, {ew}:{lon}, {time}')    


def parse_GSA(data):
    if DBG:
        print('GSA')
        print(data)
    pass

def parse_ANY(data):
    sentence = data.split(',')[0]
    print('????----------------------------------------')
    print(data)
    #print(f'????{sentence}')
    print('--------------------------------------------')
    #print(data)



JST_DIFF = 9 * 60 * 60

def get_epoch(year,month,day,hour,min,sec):
     return time.mktime((year,month,day,hour,min,sec,0,0))

#def get_local_time(year,month,day,hour,min,sec):
#    time.gmtime(get_epoch(year,month,day,hour,min,sec)  + JST_DIFF)


def get_local_time(year,month,day,hour,min,sec, onesec_after=False):
   if onesec_after:
        return time.gmtime(get_epoch(year,month,day,hour,min,sec)  + JST_DIFF + 1)
   else:
        return time.gmtime(get_epoch(year,month,day,hour,min,sec)  + JST_DIFF)


def change_GPS_baud_rate(uart, speed=HIGHSPEED_BAUD_RATE):

    cmd_str = f'$PMTK251,{speed:d}'
    parity = calculate_parity(cmd_str)
    msg = f'{cmd_str}*{parity:02X}\r\n'.encode('ascii')
    if uart.any() > 0:
         _ = uart.readline()  # dummy read
    uart.write(msg)
    change_RP2040_uart_baud_rate(uart, speed)
    if uart.any() > 0:
         print(uart.readline())
    if uart.any() > 0:
         print(uart.readline())

def change_RP2040_uart_baud_rate(uart,baudrate):

    uart.init(baudrate=baudrate, tx=Pin(16), rx=Pin(17), rxbuf=2048, timeout=1000, timeout_char=100)


def query_firm_release_info(uart):
    for _ in range(10):
        uart.readline()
    uart.write(b'$PMTK605*31\r\n')
    while True:
        print(uart.readline())

def send_test_packet(uart):
    while True:
        size=uart.write(b'$PMTK000*32\r\n')
        print(size)
        uart.flush()
        print(uart.readline())

def full_cold_start(uart):
    while True:
        size=uart.write(b'$PMTK104*37\r\n')
        print(size)
        uart.flush()
        print(uart.readline())

def full_cold_start2(uart):
    size=uart.write(b'$PMTK104*37\r\n')
    print(size)
    uart.flush()
    while True:
        print(uart.readline())

def hot_start(uart):
    while True:
        size=uart.write(b'$PMTK101*32\r\n')
        print(size)
        uart.flush()
        print(uart.readline())

def hot_start2(uart):
    size=uart.write(b'$PMTK101*32\r\n')
    print(size)
    uart.flush()
    while True:
        print(uart.readline())


def GPS_receive_all_messages(uart):

  NMEA_SEN_GLL = 1
  NMEA_SEN_RMC = 1
  NMEA_SEN_VTG = 1
  NMEA_SEN_GGA = 1
  NMEA_SEN_SGA = 1
  NMEA_SEN_GSV = 1
  GPS_API_SET_NMEA_OUTPUT(uart, NMEA_SEN_GLL,  NMEA_SEN_RMC,  NMEA_SEN_VTG,  NMEA_SEN_GGA,  NMEA_SEN_SGA,  NMEA_SEN_GSV)

def GPS_reduce_messages(uart):

  NMEA_SEN_GLL = 1
  NMEA_SEN_RMC = 1
  NMEA_SEN_VTG = 0
  NMEA_SEN_GGA = 1
  NMEA_SEN_SGA = 0
  NMEA_SEN_GSV = 0
  GPS_API_SET_NMEA_OUTPUT(uart, NMEA_SEN_GLL,  NMEA_SEN_RMC,  NMEA_SEN_VTG,  NMEA_SEN_GGA,  NMEA_SEN_SGA,  NMEA_SEN_GSV)


CMD_PMTK_API_SET_NMEA_OUTPUT = '$PMTK314'
def GPS_API_SET_NMEA_OUTPUT(uart, GLL,RMC,VTG,GGA,SGA,GSV):

  cmd = CMD_PMTK_API_SET_NMEA_OUTPUT
  cmd_str = f"{cmd},{GLL},{RMC},{VTG},{GGA},{SGA},{GSV},0,0,0,0,0,0,0,0,0,0,0,0,0"
  parity = calculate_parity(cmd_str)
  msg = f'{cmd_str}*{parity:02X}\r\n'.encode('ascii')
  size=uart.write(msg)
  print(size)


# b'$PMTK414*33\r\n'
# b'$PMTK514,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0*32\r\n'
def GPS_get_NMEA_OUTPUT(uart):
    msg = b'$PMTK414*33\r\n'
    print(f'send: {msg}')
    size= uart.write(msg)
    while True:
        if uart.any() > 0:
            msg = uart.readline()
            if 'PMTK' in msg:
                print(msg)
        else:
            time.sleep_ms(100)



#
# calculate parity 
#  in : message text (str type data)
#  out: parity  (1byte data)
#
def calculate_parity(str):
   if str[0] == '$':
      str = str[1:]
   ascii_array = str.encode('ascii')
   parity = 0
   for code in ascii_array:
      parity ^= code
   return parity


#-----------------------------------------------
#
# Lat/Lon convert functionos
#
#-----------------------------------------------


#
# convert from ddmm.mmmm  to (degree, min, sec)
# ddmm.mmmm format (dmpmf)
#
def dmpmf2dms(dmpmf):
   
   ddmm = int(dmpmf)
   mmmm = dmpmf - ddmm
   deg = int(ddmm / 100)
   mm = ddmm  - deg * 100
   ss = mmmm * 60
   return (deg, mm, ss)

#
# convert from degree to (degree,min,sec)
#
# dd.dddd to (dd, mm, ss)
#
def deg2dms(deg):
   dd = int(deg)
   mm_ss = (deg - dd) * 60
   mm = int(mm_ss)
   ss = int((mm_ss - mm) * 60)
   return (dd,mm,ss)

#
# convert from (degree,min,sec)  to degree
#
# dd.dddd to (dd, mm, ss)
#
def dms2deg(deg, min, sec):
   deg = float(deg) + float(min) / 60.0 + float(sec) / 3600.0
   return deg


#
# main function
#

main()

