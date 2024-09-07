#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


#freq: float = 30
duration: float = 0.4  # seconds

print("Playing frequency (Hz):")

playtone(392, duration)
playtone(30, 0.2)
playtone(392, duration)
playtone(30, 0.2)
playtone(587, duration)
playtone(30, 0.2)
playtone(587, duration)
playtone(30, 0.2)
playtone(660, duration)
playtone(30, 0.2)
playtone(660, duration)
playtone(30, 0.2)
playtone(587, duration*2)

playtone(30, 0.2)
playtone(523, duration)
playtone(30, 0.2)
playtone(523, duration)
playtone(30, 0.2)
playtone(494, duration)
playtone(30, 0.2)
playtone(494, duration)
playtone(30, 0.2)
playtone(440, duration)
playtone(30, 0.2)
playtone(440, duration)
playtone(30, 0.2)
playtone(392, duration*2)

#for i in range(64):
#    print(freq)
#    playtone(freq, duration)
#    freq = int(freq * 1.1)

# Turn off the PWM
quiet()
