# Lighting an LED

#### Components List
  1. LED
  1. Resistor (330 Ω (ohms))
  1. 2 - Female to male connectors
  1. 2 - Male to male connectors
 
**Note that Board numbering is used, NOT  Broadcom numbering**
1. #### Pin 11 (GPIO OUTPUT PIN)
1. #### Pin 9 (GND)



---
#### GPIO Pinout
Refer to this diagram to understand the pins we are using

**Note that Board numbering is used NOT  Broadcom numbering**
1. ##### Pin 11 (GPIO OUTPUT PIN)
1. ##### Pin 9 (GND)

<p align="center">
  <img src="../src/pics/gpio_pinout.png" alt="Diagram Schematic" width="300px">
</p>

---

#### Diagram Scematic

<p align="center">
  <img src="../src/pics/blinking_led.png" alt="Diagram Schematic" width="300px">
</p>

#### Circuit Schematic
<p align="center">
  <img src="../src/pics/blinking_led_schematic.png" alt="Circuit Schematic" width="300px">
</p>

---

### Description
Making use of the python RPi library and the GPIO methods, we can make a program that blinks an LED for a indefinate number of times or for a set number of times

##### blink.py

```py
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
```

The link to the code is [here](../../iot/basic/blink.py)