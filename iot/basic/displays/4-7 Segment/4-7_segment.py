# Displays system time in the 24h clock system
# On a 4 digit 7 segment display

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# The segment pins arranged from A to H 
segments = [11, 12, 13, 15, 16, 18, 38, 40]
for segment in segments:
   GPIO.setup(segment, GPIO.OUT)
   GPIO.output(segment, 0)

# control over the individual digit activation from right to left
digits = [22, 29, 36, 37]
for digit in digits:
   GPIO.setup(digit, GPIO.OUT)
   print(digit)
   GPIO.output(digit, 1)

# numbers dictionary
num = {
    ' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)
    }

try:
    while True:
        n = time.ctime()[11:13] + time.ctime()[14:16]
        s = str(n).rjust(4)
        for digit in range (4):
            for loop in range(7):
                GPIO.output(segments[loop], num[s[digit]][loop])
                if (int)(time.ctime()[18:19]) % 2 == 0 and digit == 1:
                    GPIO.output(40, 1)
                else:
                    GPIO.output(40, 0)
            
            GPIO.output(digits[digit], 0)
            time.sleep(0.001)
            GPIO.output(digits[digit], 1)

except KeyboardInterrupt:
   GPIO.cleanup()
   print('\nExiting...\n')