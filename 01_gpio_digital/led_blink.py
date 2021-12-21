import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)   # GPIO.BCM or GPIO.BOARD
GPIO.setup(LED_PIN, GPIO.OUT)  #GPIO.OUT or GPIO.IN

for i in range(10):
    GPIO.output(LED_PIN, GPIO.HIGH) # 1
    print("led on")
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW) # 0
    print("led out")
    time.sleep(1)

GPIO.cleanup() # GPIO 핀상태 초기화
