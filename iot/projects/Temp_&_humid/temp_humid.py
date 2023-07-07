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