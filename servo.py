import RPi.GPIO as GPIO
import time

l = 0

lServoPin = 12
rServoPin = 13
GPIO.setmode(GPIO.BCM)

GPIO.setup(lServoPin, GPIO.OUT)
GPIO.setup(rServoPin, GPIO.OUT)

lPwm = GPIO.PWM(lServoPin, 50)
rPwm = GPIO.PWM(rServoPin, 50)
lPwm.start(5)
rPwm.start(5)

# Initial positions of the servos  # 90 degrees

try:
    while l < 1:
        # Move both servos simultaneously in opposite directions
       # for i in range(45, 135):
            #l_position = 1./18.*(i)+2
           # r_position = 1./18.*(180-i)+2  # Opposite direction for the right servo
           lPwm.ChangeDutyCycle(9)
           rPwm.ChangeDutyCycle(1)
           time.sleep(1)  

       # for i in range(135, 45, -1):
           # l_position = 1./18.*(i)+2
           # r_position = 1./18.*(180-i)+2  # Opposite direction for the right servo
         # lPwm.ChangeDutyCycle(l_position)
        #  rPwm.ChangeDutyCycle(r_pos)
         # time.sleep(1)  
        
           l += 1
    
    # Return both servos to their initial positions simultaneously
           lPwm.ChangeDutyCycle(5)
           rPwm.ChangeDutyCycle(5)
           time.sleep(1) 

finally:
    lPwm.stop()
    rPwm.stop()
    GPIO.cleanup()
