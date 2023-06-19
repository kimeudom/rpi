# Vary the brightness of an LED

import RPi.GPIO as GPIO

# BOARD SETUP
GPIO.setmode(GPIO.BOARD)

# Global Duty Cycle
dutyCycle = 50

# Pins
lButton = 15
rButton = 16
led = 40

# Pins setup
GPIO.setup(rButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(lButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)

# The LED default settings
ledCtrl = GPIO.PWM(led, 60) # The output pin at frequency: 60Hz
ledCtrl.start(dutyCycle) # Starting the LED at 50% duty cycle brightness: normal

# Right if direction is True, left if direction is False
def pushed(direction: bool):
    global dutyCycle
    dutyCycle += 25 if direction == True else -25
  # Value bounds for duty cycle 1 <= x <= 99
    dutyCycle = 99 if dutyCycle >= 100 else dutyCycle
    dutyCycle = 1 if dutyCycle >= 0 else dutyCycle

    ledCtrl.ChangeDutyCycle(dutyCycle)

try:
    while True:
      if(GPIO.input(rButton) == 0):
        pushed(True)
        print("Right")

      if(GPIO.input(lButton) == 0):
        pushed(False)
        print("Left")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nExiting...\n")
