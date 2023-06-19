# The code for a servo motor
import RPi.GPIO as GPIO
from time import sleep

# Board Setup
GPIO.setmode(GPIO.BOARD)

# Servo pin
servo = 12
GPIO.setup(servo, GPIO.OUT)
servoCtrl = GPIO.PWM(servo, 50) # Servo control object running at 50Hz
servoCtrl.start(0)


try:
  print("<ctrl> + c to exit ")
  while True:
    dutyCycle = float(input("Enter Servo duty cycle: "))
    servoCtrl.ChangeDutyCycle(dutyCycle)
except KeyboardInterrupt:
  GPIO.cleanup()
  print("\nExiting...\n")