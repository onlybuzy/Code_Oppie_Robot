from PCA9685 import PCA9685
from time import sleep

import Oppie_Bot

r=Oppie_Bot.motors_move()

r.set_left(50)
r.set_right(50)
sleep(5) 