# This program toggles an LED on or off 
# it utilizes the internal pull down resistor for gpio input

import RPi.GPIO as GPIO
from time import sleep

# Led Flag state
FLAG = 0

# Board Setup Config
GPIO.setmode(GPIO.BOARD)

# Read pin
inPin = 40
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED pin
ledPin = 36
GPIO.setup(ledPin, GPIO.OUT)

i = 0

try:
  currState = GPIO.input(inPin)
  while True:
    if(currState != GPIO.input(inPin)):
      if(currState == GPIO.input(inPin)):
         # Toggle the light switch
         i+=1
         print("Toggled", i)
         if(FLAG == 0):
            GPIO.output(ledPin, 1)
            FLAG = 1
         else:
            GPIO.output(ledPin, 0)
            FLAG = 0


except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nExited\n")