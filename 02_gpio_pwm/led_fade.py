import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.out)

#PWM 인스턴스 생성, 주파수 설정 (50Hz)
# 1초에 50번 사이클이 돌게 하겠다
pwm = GPIO.PWM(LED_PIN, 50)
pwm.start(0) #duty cycle (0~100)

try:
    for j in range(3): # range(0, 3, 1)
        # 서서히 켜짐 (0~100)ㅇ
        for i in range(0, 101, 5): # start, end, step
            pwn.ChangeDutyCycle(i)
            time.sleep(0.1)
        # 서서히 꺼짐 (100~0)
        for i in range(100, -1, -5):
            pwm.ChangeDutyCycle(i)
            time.sleep(0.1)
finally:
    pwm.stop()  # pwn 종료
    GPIO.cleanup()
    print('cleanup and exit')