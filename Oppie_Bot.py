from PCA9685 import PCA9685

import atexit

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

class motors_move:
     def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4
        atexit.register(self.stopMotors)

     def set_right(self,speed):

         pwm.setDutycycle(self.PWMA, abs(speed))

         if(speed>0):

          pwm.setLevel(self.AIN1, 0)
          pwm.setLevel(self.AIN2, 1)

         if(speed<0): 

          pwm.setLevel(self.AIN1, 1)
          pwm.setLevel(self.AIN2, 0)
     
     def set_left(self,speed):

        pwm.setDutycycle(self.PWMB, abs(speed))
        
        if(speed>0):
          pwm.setLevel(self.BIN1, 0)
          pwm.setLevel(self.BIN2, 1)

        if(speed<0):  

          pwm.setLevel(self.BIN1, 1)
          pwm.setLevel(self.BIN2, 0)
      

     def stopMotors(self):
        pwm.setDutycycle(self.PWMA, 0)
        pwm.setDutycycle(self.PWMB, 0)





    
   
