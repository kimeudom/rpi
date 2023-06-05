# This program makes an LED blink 10 times before terminating
# Ensure the VCC output pin is pin 11

import RPi.GPIO as GPIO
from time import sleep



def blinker():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    for i in range(10):
        sleep(1)
        GPIO.output(11,1)
        sleep(1)
        GPIO.output(11,0)
    
    GPIO.cleanup()


blinker()

