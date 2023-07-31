import RPi.GPIO as GPIO
from RPLCD import *
from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD('PCF8574',0x27)
lcd.cursor_pos = (0,0)

try:
  lcd.write_string("Hello there")

except KeyboardInterrupt:
 sleep(.2)
 lcd.clear()
 GPIO.cleanup()
 print("\nExiting...\n")