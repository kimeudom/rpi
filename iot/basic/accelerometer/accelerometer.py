# Print out x, y and z coordinate data 

import time 
import board
import busio 
import adafruit_adxl34x
import subprocess


i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL343(i2c)

try:
    while True:
      print("%f %f %f" %accelerometer.acceleration)
      time.sleep(.1)
      subprocess.run("clear", shell=True)

except KeyboardInterrupt:
    print("\nExiting...\n")