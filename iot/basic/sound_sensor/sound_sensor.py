# A program that detects sounds that exceed a certain threshold and reports on it
# after reportin a small timeout is initiated to prevent reporting the same distrubance over and over again

import RPi.GPIO as GPIO
from time import sleep

# Board Setup
GPIO.setmode(GPIO.BOARD)

# KY-038 Digital output pin
mic = 40
GPIO.setup(mic, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Setting up a pull down resistor to prevent intermittent state reads

# Instance counter
i = 0

# Sleep delay
delay = 2


try:
  while True:
    if(GPIO.input(mic) == True):
      i += 1
      print("Sound disturbance detected, instance no %d" %i)
      sleep(delay) 

except KeyboardInterrupt:
  GPIO.cleanup()
  print("\nExiting...\n")