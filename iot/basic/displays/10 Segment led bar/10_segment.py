# Fills the bar led and repeats this indefinately

import RPi.GPIO as GPIO
from time import sleep

# Set the board numbering to pysical pin numnbers
GPIO.setmode(GPIO.BOARD)

pins = [11,13,15,16,18,19,21,22,23,24]

# PIN setup output FALSE
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)


try:
    while True:
        for pin in pins:
            GPIO.output(pin, 1)
            sleep(0.5)
        for pin in pins:
            GPIO.output(pin, 0)
    
except KeyboardInterrupt:
    GPIO.cleanup()
    print('\nExiting...\n')