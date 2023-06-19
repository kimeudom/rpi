# Controlling a RGB LED
import RPi.GPIO as GPIO

# Board Setup
GPIO.setmode(GPIO.BOARD)

# Pins
r = 11 
g = 13
b = 15

# Pin setup
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)

try:
  while True:
    GPIO.output(r, True)
    GPIO.output(g, True)
    GPIO.output(b, True)

except KeyboardInterrupt:
  GPIO.cleanup()
  print("\nExiting...\n")

