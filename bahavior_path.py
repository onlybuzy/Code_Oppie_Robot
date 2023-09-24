import Robot_Movement
from time import sleep

def straight(bot,seconds):
    bot.set_left(60)
    bot.set_right(60)
    sleep(seconds)

def turn_left(bot,seconds):
    bot.set_left(30)
    bot.set_right(60)
    sleep(seconds)
    
def turn_right(bot,seconds):
    bot.set_left(30)
    bot.set_right(10)
    sleep(seconds)

def spin_left(bot,seconds):
    bot.set_left(-30)
    bot.set_right(30)
    sleep(seconds)
def spin_right(bot,seconds):
    bot.set_left(60)
    bot.set_right(-60)
    sleep(seconds)

bot = Robot_Movement.robot_movement()
straight(bot, 1)
turn_left(bot,3.3)
spin_right(bot,0.63)
straight(bot, 3)
