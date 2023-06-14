# This code utilizes the internal step up functionality of the RPi
# There is no need to utilize breadboad step up resistors

import RPi.GPIO as GPIO
from time import sleep

# Board setup mode
GPIO.setmode(GPIO.BOARD)

# The input pin for the push button read
inPin = 40

# setting up the button
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try: 
  while True:
    sleep(0.1)
    if(GPIO.input(inPin) == 0):
      print(GPIO.input(inPin))

except KeyboardInterrupt:
  GPIO.cleanup()
  print("Exited\n")