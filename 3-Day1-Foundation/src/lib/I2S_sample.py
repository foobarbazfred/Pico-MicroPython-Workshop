#
# test source for I2S connection
#


from machine import I2S
from machine import Pin

   
SCK_PIN = 16
WS_PIN = 17
SD_PIN = 18
I2S_ID = 0

WAV_SAMPLE_SIZE_IN_BITS = 16
SAMPLE_RATE_IN_HZ = 16000    # cycle of ws (word clock)(LRCK)
BUFFER_LENGTH_IN_BYTES = 16000

buf = bytearray(BUFFER_LENGTH_IN_BYTES)

# sankaku wave
for i in range(int(len(buf)) / 2):
   if (i % 36 ) < 18:
        value  = int(255 * i / 18)
   else:
        value  = 255 - int(255 * (i - 18) / 18)

   buf[i * 2] = 0         # lower byte
   buf[i * 2 + 1] = value # upper byte


#
# sin wave
#


CENTER =  0xffff / 2 
WIDTH = 0xffff / 64

import math
for i in range(int(len(buf)) / 2):
   radian = 2 * math.pi * (i % 36) / 36
   value = int(CENTER  + WIDTH * math.sin(radian))
   buf[i * 2] = value &  0xff           #  lower byte
   buf[i * 2 + 1] = (value >> 8) & 0xff # upper byte


audio_out = I2S(I2S_ID,
    sck=Pin(SCK_PIN),
    ws=Pin(WS_PIN),
    sd=Pin(SD_PIN),
    mode=I2S.TX,
    bits=WAV_SAMPLE_SIZE_IN_BITS,
    format = I2S.MONO,
    rate=SAMPLE_RATE_IN_HZ,
    ibuf=BUFFER_LENGTH_IN_BYTES,
)

while True:
    audio_out.write(buf)



for i in range(int(len(buf)/2)):
   val = buf[i*2] + (buf[i*2+1] << 8)
   print(f"{val:d}")
   if i == 100:
       break


#
#
#
