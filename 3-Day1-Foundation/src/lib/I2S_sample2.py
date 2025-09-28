#
#original source:
#   https://github.com/miketeachman/micropython-i2s-examples/blob/master/examples/play_tone.py
#

#
# I2S Sin wave play test for Raspberry Pi Pico 2 with MAX98357
#

import os
import math
import array
from machine import Pin
from machine import I2S


# ======= I2S CONFIGURATION for Raspberry Pi Pico=======
SCK_PIN = 16
WS_PIN = 17
SD_PIN = 18
I2S_ID = 0
BUFFER_LENGTH_IN_BYTES = 2000
# ======= I2S CONFIGURATION =======


# ======= AUDIO CONFIGURATION =======
SAMPLE_RATE_IN_HZ = 8_000           # sampling rate 8kHz (most)
                                    # The lowest supported sample rate of the MAX98357 is 8 kHz.
TONE_FREQUENCY_IN_HZ = 440
SAMPLE_SIZE_IN_BITS = 16            #  16bit/sound
FORMAT = I2S.MONO  # only MONO supported in this example
# ======= AUDIO CONFIGURATION =======


#
# generate sin wave
# generate monoral , 16bit / sound
# 
#
def make_tone_signed_16b(rate, frequency, volume_reduction_factor):
    # create a buffer containing the pure tone samples
    samples_per_cycle = rate // frequency
    samples = array.array('h', [0] * samples_per_cycle)  # 'h' : signed short (2bytes)
    tone_value_range = (pow(2, SAMPLE_SIZE_IN_BITS) - 1) // volume_reduction_factor 
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

volume_reduction_factor = 7
samples = make_tone_signed_16b(SAMPLE_RATE_IN_HZ, TONE_FREQUENCY_IN_HZ, volume_reduction_factor)
print("==========  START PLAYBACK ==========")
try:
    while True:
        num_written = audio_out.write(samples)
except (KeyboardInterrupt, Exception) as e:
    print("caught exception {} {}".format(type(e).__name__, e))

# cleanup
audio_out.deinit()
del audio_out
print("Done")
