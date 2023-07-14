# Passive InfRared Sensor
It has two main components: 
- Pyroelectric sensor
  It produces an electric charge when exposed to infrared rays. Change in current pattern indicates movement in front of the sensor.
- Fresnel lens
  Focuses the IR rays onto the sensor.

---

Implimenting a basic motion sensor that detects movement in front of the device, when this happens, an LED blinks to indicate movement.

#### Components List
  1. Motion Sensor [PIR HC-SR502]
  1. 4 - Female to male connectors
  1. 1 - LED
  1. 1 - 330Ω Resistor
 
**Note that Board numbering is used, NOT  Broadcom numbering**

1. #### Pin 2 (5.0V Vcc)
1. #### Pin 37 (LED)
1. #### Pin 39 (GND)
1. #### Pin 40 (Motion Sensor Output [the Pi's input])

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
  <img src="../src/pics/motion sensor.png" alt="Diagram Schematic" width="300px">
</p>

#### Circuit Schematic
<p align="center">
  <img src="../src/pics/motion sensor_schematic.png" alt="Circuit Schematic" width="300px">
</p>

---

### Description
When a target moves before the sensor, the program notes this and a LED blinks to signify movement.

###### movement.py
```py
# Uses a HC-SR501 sensor to detect movement output

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

# Alert LED
led = 37
GPIO.setup(led, GPIO.OUT)

# Passive Infrared output pin
pir = 40
GPIO.setup(pir, GPIO.IN)

curr_state = 0
counter = 1

def blink():
   GPIO.output(led, 1)
   sleep(1)
   GPIO.output(led, 0)

try:
    while True:
      curr_state = GPIO.input(pir)
      if curr_state == 1:
         counter += 1
         blink()
         print('detected movement' , counter)
         sleep(1)



    
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nExiting...\n")
```

Code [link](../../iot/basic/motion_sensor/motion.py)