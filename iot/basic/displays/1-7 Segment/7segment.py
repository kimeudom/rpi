# Controling a 7 segment display
# Component: 5011AS

import RPi.GPIO as GPIO
from time import sleep

# Board Setup
GPIO.setmode(GPIO.BOARD)

# Pi pins
aPin = 11
bPin = 13
cPin = 40
dPin = 38
ePin = 31
fPin = 29
gPin = 15
hPin = 16

GPIO.setup(aPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)
GPIO.setup(cPin, GPIO.OUT)
GPIO.setup(dPin, GPIO.OUT)
GPIO.setup(ePin, GPIO.OUT)
GPIO.setup(fPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)

# Segment Pins
A, B, C, D, E, F, G = aPin, bPin, cPin, dPin, ePin, fPin, gPin

# Numbers
zero = [A, B, C, D, E, F]
one = [B, C]
two = [A, B, G, E, D]
three = [A, B, G, C, D]
four = [B, C, G, F]
five = [A, F, G, C, D]
six = [A, F, E, D, C, G]
seven = [A, B, C]
eight = [A, B, C, D, E, F, G]
nine = [A, B, C, D, G, F]

numbers = [
    zero, one, two, three, four,
    five, six, seven, eight, nine
]

try:
    while True:
        for i in numbers:
            for j in i:
                GPIO.output(j, 1)
            sleep(1)
            for j in i:
                GPIO.output(j, 0)

        sleep(10)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nExitting...\n")
