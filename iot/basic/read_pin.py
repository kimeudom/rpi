## reads pin output and relays that back

import RPi.GPIO as gpio
from time import sleep

# Board setup
gpio.setmode(gpio.BOARD)

# Pin setup
inPin = 40
gpio.setup(inPin, gpio.IN)

try:
  while 1:
     sleep(1)
     readVal = gpio.input(inPin)
     print(readVal)
     sleep(1)

except KeyboardInterrupt:
    gpio.cleanup()