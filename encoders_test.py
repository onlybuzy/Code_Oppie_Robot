import Oppie_Bot
import time
import logging

from gpiozero import DigitalInputDevice



class EncoderCounter(object):
    def __init__(self, pin):
        self._value = 0
        encoder = DigitalInputDevice(pin)
        encoder.when_activated = self._increment
        encoder.when_deactivated = self._increment
    def reset(self):
        self._value = 0
    def _increment(self):
        self._value += 1
    @property
    def value(self):
        return self._value


r=Oppie_Bot.motors_move()


enc_1=EncoderCounter(4)

enc_2=EncoderCounter(17)


stop_at_time = time.time() + 1


r.set_left(50) 
r.set_right(50)

while time.time()<stop_at_time:
     print("e1 {} e2 {}".format(enc_1.value, enc_2.value))
     time.sleep(0.05)