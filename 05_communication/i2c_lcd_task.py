from lcd import drivers
import time
import datetime
import Adafruit_DHT

display = drivers.Lcd()
sensor = Adafruit_DHT.DHT11
PIN = 18

try:
    while True:
        now = datetime.datetime.now()
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        display.lcd_display_string(now.strftime("%x%X"), 1)
        display.lcd_display_string(f"{temperature:.1f}*C, {humidity:.1f}%", 2)
        time.sleep(1)

finally:
    print("Cleaning up!")
    display.lcd_clear()