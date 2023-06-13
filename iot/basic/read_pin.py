## reads pin output and relays that back

import RPi.GPIO as GPIO
from time import sleep

# Board setup
gpio.setmode(GPIO.BOARD)

# Pin setup
inPin = 40
GPIO.setup(inPin, GPIO.IN)

try:
  while 1:
     sleep(1)
     readVal = GPIO.input(inPin)
     print(readVal)
     sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()