
import pylcd_i2c
from time import sleep

lcd_address = 0x27
port = 1
reverse = pylcd_i2c.PYLCD_LCD2004_BL  # "LCD2004" board where lower 4 are commands, but backlight is pin 3



lcd = pylcd_i2c.lcd(addr = lcd_address, port=port, reverse=reverse)

while 1:
        lcd.lcd_puts("Hello, World!", 2)
        sleep(5)
