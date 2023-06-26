# A program that measues the distance between the front of a HC_SRQ4 ultrasonic sensor to a target within range

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Pins
echo = 40
trig = 38

GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# Sends a trigger signal to the sensor requesting it to do it's magic
def sendTrigger():
  GPIO.output(trig, 0)
  time.sleep(2E-6)
  GPIO.output(trig, 1)
  time.sleep(10E-6)
  GPIO.output(trig, 0)

# Returns the time delta of a round trip time for the sensor's signal
def delta() -> float:
  while GPIO.input(echo) == 0:
    pass
  start = time.time()
  while GPIO.input(echo) == 1:
    pass
  end = time.time()

  # Converting from micro seconds to seconds
  return (end - start) * 1E6

# Returns the distance between the sensor and the object in centimeters
def distance(delta: float) ->float:
  # Halfing the time taken
  delta *= 0.5
  speed = 330 #  330m/s

  # Converting the distance to centimeters
  return (delta * speed) * 100

try: 
  while True:
    sendTrigger()
    print(distance(delta()), "cm")
    time.sleep(.5)

except KeyboardInterrupt:
  GPIO.cleanup()
  print("\nExiting...\n")