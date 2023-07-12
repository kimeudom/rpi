# Displays system time in the 24h clock system
# On a 4 digit 7 segment display

import RPi.GPIO as GPIO
import sys
import time, datetime

delay = 0.005

GPIO.setmode(GPIO.BOARD)

# The segment pins arranged from A to H 
segments = [18, 19, 21, 22, 23, 24, 26, 29]
for segment in segments:
   GPIO.setup(segment, GPIO.OUT)
   GPIO.output(segment, 0)

# control over the individual digit activation from right to left
digits = [11, 13, 15, 16]
for digit in digits:
   GPIO.setup(digit, GPIO.OUT)
   GPIO.output(digit, 1)

num = [[1,1,1,1,1,1,0],\
       [0,1,1,0,0,0,0],\
       [1,1,0,1,1,0,1],\
       [1,1,1,1,0,0,1],\
       [0,1,1,0,0,1,1],\
       [1,0,1,1,0,1,1],\
       [1,0,1,1,1,1,1],\
       [1,1,1,0,0,0,0],\
       [1,1,1,1,1,1,1],\
       [1,1,1,1,0,1,1]]

def showDisplay(digit):
   for i in range(0,4):
      sel = [1,1,1,1]
      sel[i] = 0
      GPIO.output(digits, sel)

      if digit[i].replace(".", "") == " ":
        GPIO.output(segments, 0)
        continue
    
      numDisplay = int(digit[i].replace(".", ""))
      GPIO.output(segments[:-1], num[numDisplay]) # Activating the segments

      if digit[i].count(".") == 1:
        GPIO.output(segments[-1], 1)
      else:
        GPIO.output(segments[-1], 0)
    
      time.sleep(delay)

def getTime():
    now = datetime.datetime.now()
    outString = str(now.hour) + str(now.minute)
    print("Time : ", outString)

    arr = list(outString)

    for i in range(len(arr)):
       if arr[i] == "." : arr[i - 1] += arr[i]
    
    while "." in arr: arr.remove(".")

    return arr

try:
    while True:
       showDisplay(getTime())

except KeyboardInterrupt:
   GPIO.cleanup()
   print('\nExiting...\n')