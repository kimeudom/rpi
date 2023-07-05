import LCD1602 as lcd
import time 

lcd.init(0x27, 1)

try:
  while True:
    lcd.write(0,0, 'Hi!')
    lcd.write(0,1, ':)')

except KeyboardInterrupt:
  time.sleep(0.2)
  lcd.clear()
  print('\nExiting...\n')