# CO2センサの接続

- Senserion SCD41
- 温度、湿度、CO2濃度

デバイス接続テスト
```
self.i2c = I2C(id=bus, scl=Pin(sclpin), sda=Pin(sdapin), freq=400000)
>>> hex(i2c.scan()[0])
'0x62'
```
Sensiron用のコンパクトなドライバがないので、今回は最小限のコードを書きました。一般的なセンサはレジスタ用のアドレスが割り振られていて、指定されたアドレスのレジスタにパラメータを書き込んだり、レジスタから値を読み込むことでデバイスとの通信を行います。Sensirionの場合、レジスタの概念がなく、コマンドの送受信でセンサを制御します。

```
#
# Driver for SCD41
#

#// reference documents and source:
#  https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf
#  https://github.com/adafruit/Adafruit_CircuitPython_SCD4X/blob/main/adafruit_scd4x.py
#  https://crates.io/crates/scd4x
#  https://github.com/hauju/scd4x-rs
#  https://github.com/adafruit/Adafruit_CircuitPython_SCD4X


from machine import Pin
from machine import I2C

SCD41_ADDRESS = 0x62

CMD_START_PERIODIC_MEASURMENT = bytes((0x21, 0xb1,))
CMD_STOP_PERIODIC_MEASURMENT = bytes((0x3f, 0x86,))
CMD_READ_MEASUREMENT = bytes((0xec, 0x05,))
CMD_GET_SERIAL_NUMBER = bytes((0x36, 0x82,))
CMD_GET_DATA_READY_STATUS =  bytes((0xe4, 0xb8,))


# wait for 5 seconds after start periodic measurement
def init_sensor(i2c):
    stat = stop_periodic_measurement(i2c)
    stat = start_periodic_measurement(i2c)
    return stat

def get_serial_number(i2c, verbose=False):
    if verbose:
        print("--- get serial number -----");
    stat = i2c.writeto(SCD41_ADDRESS, CMD_GET_SERIAL_NUMBER)
    time.sleep_ms(1)
    data = i2c.readfrom(SCD41_ADDRESS, 9)  # get (2 bytes  + 1 CRC) * 3
    return data

def start_periodic_measurement(i2c, verbose=False):
    if verbose:
        print("--- start periodic measurement ----");
    stat = i2c.writeto(SCD41_ADDRESS, CMD_START_PERIODIC_MEASURMENT)
    return stat

def stop_periodic_measurement(i2c, verbose=False):
    if verbose:
        print("--- stop periodic measurement ----");
    stat = i2c.writeto(SCD41_ADDRESS, CMD_STOP_PERIODIC_MEASURMENT)
    time.sleep_ms(500)          # wait for Max. command duration
    return stat

def get_data_ready_status(i2c):
    stat = i2c.writeto(SCD41_ADDRESS, CMD_GET_DATA_READY_STATUS)
    time.sleep_ms(1)
    data = i2c.readfrom(SCD41_ADDRESS, 3)   # get (2 bytes  + 1 CRC) * 3
    value = (data[0] << 8) | data[1]
    if value & 0x7ff == 0:   # If the least significant 11 bits of word[0] are: 0 
       return False          #    -> data not ready 
    else:
       return True

def read_measurement(i2c, verbose=False):

    if verbose:
        print("---- read measure ment -----");

    # check data is ready
    if get_data_ready_status(i2c) is False:
       return None, None, None

    stat = i2c.writeto(SCD41_ADDRESS, CMD_READ_MEASUREMENT)
    time.sleep_ms(1)
    data = i2c.readfrom(SCD41_ADDRESS, 9)   # get (2 bytes  + 1 CRC) * 3

    #// calculate CO2
    co2 = (data[0] << 8) | data[1] 

    #// calculate Temperature
    val = data[3]  << 8 | data[4] 
    temp = -45.0 + 175.0 * val / 65535.0  #   // 65535 = 0xffff

    #// calculate Humidity
    val = (data[6]  << 8) | data[7] 
    hum = 100.0 * val  / 65535.0         # ;  // 65535 = 0xffff
    return temp, hum, co2


def main():

    #
    # setup
    #
    
    # setup i2c bus for sensor
    i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=20_000)
    
    # >>> hex(i2c.scan()[0])
    # '0x62'
    
    init_sensor(i2c)
    time.sleep(5)        # wait until sensor is ready

    #
    # loop
    #
    
    while True:
        temp, hum, co2 = read_measurement(i2c)
        if temp is None:
            print(f"temp: --.-- C, hum: --.-- %, CO2: ---- ppm")           
        else:
            print(f"temp: {temp:.2f}C, hum: {hum:.2F} %, CO2: {co2} ppm")
        time.sleep(60)

    
if __name__ == '__main__':    
   main()    
    

#
#
#

```

### 参考資料
- Sensirion SDC41 Porcut
  - https://sensirion.com/jp/products/catalog/SCD41
- Sensirion SCD4x DataSheet
  - https://sensirion.com/media/documents/48C4B7FB/67FE0194/CD_DS_SCD4x_Datasheet_D1.pdf
- Sensirion Drvier
  - https://github.com/Sensirion/python-i2c-scd/tree/master/sensirion_i2c_scd/scd4x
