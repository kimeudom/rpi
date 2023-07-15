# Temperature and Humidity

# Objectives
Collect real time ambient temperature and humidity of the room you are in and display the results on an LCD screen using a Raspberry Pi4.
<p align='center'>
<img src='../prj%20gallary/temp_humid/DSC00202.JPG' width='300px'>
<img src='../prj%20gallary/temp_humid/DSC00189.JPG' width='300px'>
<img src='../prj%20gallary/temp_humid/DSC00239.JPG' width='300px'>
</p>

[Project Gallary](../prj%20gallary/temp_humid/)

---

## Implimentation Diagram
<p align='center'>
<img src='../src/pics/temp_humid.png' width='800px'>
</p>

# PreRequisites
## 1. DHT 11 Sensor

  ### Software Dependencies
  - pip

      Pip python package manager
      ```
      sudo apt-get install pip
      ```

  - The DHT11 library
      ```
      pip install dht11
      ```

## 2. [LCD 1602A with LCM 1602 I2C adapter.](<../md files/lcdDisp.md>) 
  Refer to this [page](<../md files/lcdDisp.md>) to get things started.

<br>
<br>
<br>

# Code

Ensure all libraries are isntalled and the [LCD1602.py](../../iot/projects/Temp_&_humid/LCD1602.py) file is in the same operating directory as the code below.


###### temp_humid.py
```py
import RPi.GPIO as GPIO
import dht11
import LCD1602 as lcd
from time import sleep

# Board setup
GPIO.setmode(GPIO.BOARD)

# DHT11 output pin setup
dht = dht11.DHT11(pin = 40)

lcd.init(0x27, 1)

try:
  while True:
    res = dht.read()
    if res.is_valid():
      lcd.write(0,0, "Temp: ")
      lcd.write(6,0, str(res.temperature))
      lcd.write(11,0, 'C')
      lcd.write(0,1, "Humidity: ")
      lcd.write(10,1, str(res.humidity))
      print(f'Temperature {res.temperature}C\nHumidity{res.humidity}')
    
    sleep(5)

except KeyboardInterrupt:
  sleep(0.2)
  lcd.clear()
  GPIO.cleanup()
  print('\nExiting...\n')
```
Code [link](../../iot/projects/Temp_&_humid/temp_humid.py).