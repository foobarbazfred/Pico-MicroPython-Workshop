#
# i2s sin wave play test 
# ok  (signed value)
#

import os
import time
import math
import array
from machine import Pin
from machine import I2S

SCK_PIN = 16
WS_PIN = 17
SD_PIN = 18
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 1024

SAMPLE_RATE_IN_HZ = 8_000      # The lowest supported sample rate of MAX98357
SAMPLE_SIZE_IN_BITS = 16       #  16bit/sound
FORMAT = I2S.MONO              # only MONO supported in this example
FREQ_A440 = 440

#
# create a buffer containing the pure tone samples
#

MAX_VOLUME = 0xff

def make_tone_signed_16b(rate, frequency, volume):
    samples_per_cycle = rate // frequency
    samples = array.array('h', [0] * samples_per_cycle)  # 'h' : signed short (2bytes)
    # value_range : max value of posivtive value  ; -tone_value_range -- 0 -- +tone_value_range
    tone_value_range = (pow(2, (SAMPLE_SIZE_IN_BITS - 1)) - 1) * volume // MAX_VOLUME
    #print('tone_value_range', tone_value_range)
    for i in range(samples_per_cycle):
        samples[i] = int(tone_value_range * math.sin(2 * math.pi * i / samples_per_cycle))
    return samples


audio_out = I2S(
    I2S_ID,
    sck = Pin(SCK_PIN),
    ws = Pin(WS_PIN),
    sd = Pin(SD_PIN),
    mode = I2S.TX,
    bits = SAMPLE_SIZE_IN_BITS,
    format = FORMAT,
    rate = SAMPLE_RATE_IN_HZ,
    ibuf = BUFFER_LENGTH_IN_BYTES,
)

freq = FREQ_A440

for volume in range(0x00, 0xFF, 0x10):
    tone_data = make_tone_signed_16b(SAMPLE_RATE_IN_HZ, freq, volume)
    print(f'vol: {volume:02x}')
    print(tone_data)
    for _ in range(int(freq/8)):   # play for 0.12sec
        _ = audio_out.write(tone_data)
    time.sleep(0.1)

machine.reset()







