# This program toggles an LED on or off
# it utilizes the internal pull down resistor for gpio input

import RPi.GPIO as GPIO

# Led Flag state
FLAG = 0

# The push button state
currState = 1
currStateOld = 1

# Board Setup Config
GPIO.setmode(GPIO.BOARD)

# Read pin
inPin = 40
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED pin
ledPin = 36
GPIO.setup(ledPin, GPIO.OUT)

i = 0

try:
    while True:
        currState = GPIO.input(inPin)
        if (currState == 1 and currStateOld == 0):
            # Toggle the led
            i += 1
            print("Toggled ", i)
            FLAG = not FLAG
            GPIO.output(ledPin, FLAG)

        currStateOld = currState

except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nExited\n")
