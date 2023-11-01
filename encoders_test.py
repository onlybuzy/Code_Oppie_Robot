import Oppie_Bot
import time
import logging

from gpiozero import DigitalInputDevice


logger=logging.getLogger("test_encoders")

class EncoderCounter(object):
    def __init__(self, pin_number):
        self.pulse_count = 0
        self.device = DigitalInputDevice(pin=pin_number)
        self.device.pin.when_changed = self.when_changed
    def when_changed(self, _, state):
        self.pulse_count += 1
    

r=Oppie_Bot.motors_move()


enc_1=EncoderCounter(4)
enc_2=EncoderCounter(17)
enc_3=EncoderCounter(27)

stop_at_time = time.time() + 2


logging.basicConfig(level=logging.INFO)
r.set_left(50) 
r.set_right(50)

while time.time()<stop_at_time:
     logger.info(f"enc_1: {enc_1.pulse_count} enc_2: {enc_2.pulse_count} enc_3: {enc_3.pulse_count}")
     time.sleep(0.01)