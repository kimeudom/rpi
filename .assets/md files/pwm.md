# Pulse Width Modulation (PWM)

This is a method of controlling the average power delivery by an electrical signal by switching the supply, between 0% and 100%, at a rate faster than it takes the load to change significantly. By varying the pulse width of a signal to effectively vary the power delivery on a load.

The signal consists of a series of pulses with a fixed frequency, where the duration of each pulse is adjusted to achieve the desired outcome.

## Duty Cycle

The ratio of the pulse width to the total period is referred to as the ***Duty Cycle***
If the frequency used in PWM is appropriate, you can think of the duty cycle as a percentage of the total possible supply of power.
For our use case, GPIO pin output is **3.3V**, a duty cycle of **50%** is effectively **1.65V**.

###### Duty cycle example
<p align="center">
<img src="../src/pics/Duty_Cycle_Examples.png" width="300px">
</p>

## Frequency
Frequency varys according to load an application. 

Choosing a switching frequency that is too high for the application results in smooth control of the load, but may cause premature failure of the mechanical control components. Selecting a switching frequency that is too low for the application causes oscillations in the load.

e.g. In home electricity supply, frequency is usually 50Hz to 60Hz, just fast enough that the human eye cannot percieve flickering.


### Applications of PWM: 

1. **Lighting control: PWM is utilized in dimmable LED lighting systems to adjust the brightness levels. By changing the duty cycle of the PWM signal driving the LED, the average current flowing through the LED can be modified, resulting in varied illumination levels. (We will see an implementation of this below)**

1. Motor control: PWM is widely employed to control the speed of electric motors, such as those found in robotics, drones, and industrial machinery. By varying the duty cycle of the PWM signal, the average voltage or current supplied to the motor can be adjusted, thereby controlling its rotational speed.

1. Power regulation: PWM is utilized in power electronic systems, such as DC-DC converters and voltage regulators, to regulate the output voltage or current. By adjusting the duty cycle, the effective power delivered to the load can be controlled.

---

# LED LIGHT CONTROL
By implimenting PWM, we want to vary the brightness of an LED between 5 levels.

1. [5] Very bright
1. [4] Bright
1. [3] Normal
1. [2] Dim
1. [1] Very Dim

#### Components List
  1. LED
  1. Resistor (330 Ω (ohms))
  1. 2 - Push buttons
  1. 5 - Female to male connectors
  1. 3 - Male to male connectors
 
**Note that Board numbering is used, NOT  Broadcom numbering**
1. #### Pin 9 (GND)
1. #### Pin 15 (Left Button Input)
1. #### Pin 16 (Right button Input)
1. #### Pin 17 (3.3V)
1. #### Pin 40 (LED CONTROL)



---
#### GPIO Pinout
Refer to this diagram to understand the pins we are using

**Note that Board numbering is used NOT  Broadcom numbering**

<p align="center">
  <img src="../src/pics/gpio_pinout.png" alt="Diagram Schematic" width="300px">
</p>

---

#### Diagram Scematic

<p align="center">
  <img src="../src/pics/PWM%20LED.png" alt="Diagram Schematic" width="300px">
</p>

#### Circuit Schematic
<p align="center">
  <img src="../src/pics/PWM%20LED_schematic.png" alt="Circuit Schematic" width="300px">
</p>

---

### Description
Using the right and left buttons, we should be able to vary the brighness of an LED using PWM.

Right button - INCRASE BRIGHTNESS
Left button  - DECREASE BRIGTNESS

###### pwm_led.py

```py
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
```

Code [Link]()
