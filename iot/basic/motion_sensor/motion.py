# Uses a HC-SR501 sensor to detect movement output

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# Alert LED
led = 37
GPIO.setup(led, GPIO.OUT)

# Passive Infrared output pin
pir = 40
GPIO.setup(pir, GPIO.IN)

curr_state = 0
counter = 1

def blink():
   GPIO.output(led, 1)
   sleep(1)
   GPIO.output(led, 0)

try:
    while True:
      curr_state = GPIO.input(pir)
      if curr_state == 1:
         counter += 1
         blink()
         print('detected movement' , counter)
         sleep(1)



    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nExiting...\n")