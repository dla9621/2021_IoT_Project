import spidev
import RPi.GPIO as GPIO
import time

LED_PIN = 17
spi = spidev.SpiDev()

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
spi.open(0, 0)

spi.max_speed_hz = 100000

def analog_read(channel):
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        ldr_value = analog_read(0)
        if ldr_value <= 700:
            GPIO.output(LED_PIN, GPIO.HIGH)
            print("ON")
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            print("OFF")
        time.sleep(0.5)
finally:
    spi.close()
    GPIO.cleanup()