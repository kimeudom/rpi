# Ask the user for input, blink the light the set number of times
# re-prompt
import RPi.GPIO as gpio
from time import sleep

def blink(n):
    gpio.setmode(gpio.BOARD)
    gpio.setup(11, gpio.OUT)
    
    # loop the input
    for i in range(n):
        gpio.output(11, 1)
        sleep(1)
        gpio.output(11, 0)
        sleep(1)

    gpio.cleanup()


def init():
    # Default input setting to enter the loop
    n = 1;
    while n > 0:
        n = int(input("Enter the number of times to blink the light (0 = exit): "))
        blink(n)


init();
