import RPi.GPIO as GPIO
import time

LED_RED = 7
LED_YELLOW = 8
LED_GREEN = 9
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)

GPIO.output(LED_RED, GPIO.HIGH)
print("led red on")
time.sleep(2)
GPIO.output(LED_RED, GPIO.LOW)
print("led red off")
GPIO.output(LED_YELLOW, GPIO.HIGH)
print("led yellow on")
time.sleep(2)
GPIO.output(LED_YELLOW, GPIO.LOW)
print("led yellow off")
GPIO.output(LED_GREEN, GPIO.HIGH)
print("led green on")
time.sleep(2)
GPIO.output(LED_GREEN, GPIO.LOW)
print("led green off")

GPIO.cleanup()