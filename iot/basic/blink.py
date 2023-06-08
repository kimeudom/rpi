# Makes an LED connected to GPIO Pin 11 to blink ON and OFF indefinately
# until the user suplies a keyboard interrupt (<CTRL> + <C>)
import RPi.GPIO as GPIO
from time import sleep

outPin = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin, GPIO.OUT)

# Makes the LED blink ON and OFF in 2s


def blinker():
    sleep(1)
    GPIO.output(outPin, 1)
    sleep(1)
    GPIO.output(outPin, 0)


try:
    while (True):
        blinker()

except KeyboardInterrupt:
    GPIO.cleanup()
