# Motion Sensor Project

# Objective
Detect motion in the target area and note the number of disturbances in the area.
#### Disclaimer
This implimentation has a 5s timeout after a disturbance has been detected. The next disturbance can only be recorded after the 5s has elapsed.

<p align='center'>
<img src='../prj%20gallary/motion_detection/DSC00486.JPG' width='300px'>
<img src='../prj%20gallary/motion_detection/DSC00503.JPG' width='300px'>
<img src='../prj%20gallary/motion_detection/DSC00482.JPG' width='300px'>
</p>

[Project Gallery](../prj%20gallary/motion_detection/)
---

## Implimentation Diagram
<p align="center">
<img src="../src/pics/motion_sensor_prj.png" width="800px">
</p>

# Prerequisites

## 1. [PIR sensor HC-SR501](../md%20files/motion_sensor.md)
  Refer to this [page](../md%20files/motion_sensor.md) to setup the motion sensor.

## 2. [LCD 1602A with LCM 1602 I2C adapter.](<../md files/lcdDisp.md>) 
  Refer to this [page](<../md files/lcdDisp.md>) to get things started.

# Code
Ensure all libraries are installed and the [LCD1602.py](../../iot/projects/Temp_&_humid/LCD1602.py) file is in the same operating directory as the code below.


###### motion_detection.py
```py
# Uses a HC-SR501 sensor to detect movement output

import RPi.GPIO as GPIO
import LCD1602 as lcd
from time import sleep

# Board setup
GPIO.setmode(GPIO.BOARD)

lcd.init(0x27, 1)

# Alert LED
led = 37
GPIO.setup(led, GPIO.OUT)

# Passive Infrared output pin
pir = 40
GPIO.setup(pir, GPIO.IN)

curr_state = 0
counter = 1

def showPrompt(instance : int):
   lcd.write(0,0, "Motion detected")
   output = "Instance #: " + str(instance)
   lcd.write(0,1, output)

try:
    while True:
      curr_state = GPIO.input(pir)
      if curr_state == 1:
         counter += 1
         showPrompt(counter)
         sleep(4)



    
except KeyboardInterrupt:
    GPIO.cleanup()
    sleep(.2)
    lcd.clear()
    print("\nExiting...\n")
```
Code [link](../../iot/projects/motion_detection/motion_detection.py)