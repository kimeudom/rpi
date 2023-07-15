# Uses a HC-SR501 sensor to detect movement output

import RPi.GPIO as GPIO
import LCD1602 as lcd
from time import sleep

# Board setup
GPIO.setmode(GPIO.BOARD)

lcd.init(0x27, 1)

# Alert LED
led = 37
GPIO.setup(led, GPIO.OUT)

# Passive Infrared output pin
pir = 40
GPIO.setup(pir, GPIO.IN)

curr_state = 0
counter = 1

def showPrompt(instance : int):
   lcd.write(0,0, "Motion detected")
   output = "Instance #: " + str(instance)
   lcd.write(0,1, output)

try:
    while True:
      curr_state = GPIO.input(pir)
      if curr_state == 1:
         counter += 1
         showPrompt(counter)
         sleep(4)



    
except KeyboardInterrupt:
    GPIO.cleanup()
    sleep(.2)
    lcd.clear()
    print("\nExiting...\n")