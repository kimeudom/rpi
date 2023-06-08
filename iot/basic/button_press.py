# This program outputs a prompt that says button press if a button on the breadboard circuit is pressed

import RPi.GPIO as gpio 
from time import sleep

# Global pin number
inPin = 40


gpio.setmode(gpio.BOARD)
gpio.setup(inPin, gpio.IN)

while(1):
    sleep(1)
    val = gpio.input(inPin)
    print(val)


gpio.cleanup()