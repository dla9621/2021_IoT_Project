import RPi.GPIO as GPIO
import time

BUZZER_PIN_MAIN1 = 8
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN_MAIN1, GPIO.OUT)
pwm_main = GPIO.PWM(BUZZER_PIN_MAIN1, 262)

melody = [1,262, 294, 330, 349, 392, 440]
main = [5,5,6,6,5,5,3,0,5,5,3,3,2,2,2,0,5,5,6,6,5,5,3,3,5,3,2,3,1,1,1,0]

try:
    for i in range(0,len(main)):
        pwm_main.ChangeFrequency(melody[main[i]]*4)
        pwm_main.start(90)
        time.sleep(0.4)

finally:
    GPIO.cleanup()