# A program that showcases the importance of a step up or step down resistor
# To avoid the indeterminate state
# The program will work independent of which implementation of step up or step down is used

import RPi.GPIO as GPIO
from time import sleep

# The input read pin 
inPin = 40

# Board setup and config
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN)

try:
  pinState = GPIO.input(inPin)
  while(1):
    if(pinState != GPIO.input(inPin)):
      print(GPIO.input(inPin))
      # Momentary pause because the loop executes multiple times a second
      sleep(.25)

except KeyboardInterrupt:
  GPIO.cleanup()