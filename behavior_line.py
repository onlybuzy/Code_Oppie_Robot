from PCA9685 import PCA9685
from time import sleep

import Robot

r=Robot.robot_movement()

r.set_left(50)
r.set_right(50)
sleep(5) 