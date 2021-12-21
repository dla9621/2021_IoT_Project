import RPi.GPIO as GPIO

LED_PIN_1 = 4
LED_PIN_2 = 17
LED_PIN_3 = 27
SWITCH_PIN_1 = 14
SWITCH_PIN_2 = 15
SWITCH_PIN_3 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(SWITCH_PIN_1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(SWITCH_PIN_3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        val_1 = GPIO.input(SWITCH_PIN_1)
        print(val_1)
        GPIO.output(LED_PIN_1, val_1)

        val_2 = GPIO.input(SWITCH_PIN_2)
        print(val_2)
        GPIO.output(LED_PIN_2, val_2)

        val_3 = GPIO.input(SWITCH_PIN_3)
        print(val_2)
        GPIO.output(LED_PIN_3, val_3)

finally:
    GPIO.cleanup()
    print('cleanup and exit')