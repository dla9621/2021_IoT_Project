import RPi.GPIO as GPIO
import time

PIR_PIN = 20 # PIR 센서
BUZ_PIN = 16 # 피에조 부저
LED_RED = 19 # 빨간색 LED
LED_YEL = 26 # 노란색 LED
LED_GRE = 21 # 초록색 LED

#                 A  B   C   D   E   F  G
SEGMENT_PINS_1 = [4, 17, 18, 15, 14, 3, 2]
#                 A   B  C   D   E   F   G
SEGMENT_PINS_2 = [10, 9, 25, 24, 23, 22, 27]
#                 A  B   C   D  E  F  G
SEGMENT_PINS_3 = [6, 13, 12, 7, 8, 5, 11]

stopwatch = 0 # 스톱워치 초기값 설정

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)
GPIO.setup(BUZ_PIN, GPIO.OUT)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_YEL, GPIO.OUT)
GPIO.setup(LED_GRE, GPIO.OUT)

for segment in SEGMENT_PINS_1:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

for segment in SEGMENT_PINS_2:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

for segment in SEGMENT_PINS_3:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

data = [[0, 0, 0, 0, 0, 0, 0],  # 빈 화면
        [1, 1, 1, 1, 1, 1, 0],  # 0 
        [0, 1, 1, 0, 0, 0, 0],  # 1
        [1, 1, 0, 1, 1, 0, 1],  # 2
        [1, 1, 1, 1, 0, 0, 1],  # 3
        [0, 1, 1, 0, 0, 1, 1],  # 4
        [1, 0, 1, 1, 0, 1, 1],  # 5
        [1, 0, 1, 1, 1, 1, 1],  # 6
        [1, 1, 1, 0, 0, 0, 0],  # 7
        [1, 1, 1, 1, 1, 1, 1],  # 8
        [1, 1, 1, 0, 0, 1, 1]]  # 9

def display1(number): # 숫자 / 10초대
    for i in range(7):
        GPIO.output(SEGMENT_PINS_1[i], data[number+1][i])

def display2(number): # 숫자 / 1초대
    for i in range(7):
        GPIO.output(SEGMENT_PINS_2[i], data[number+1][i])

def display3(number): # 숫자 / 0.1초대
    for i in range(7):
        GPIO.output(SEGMENT_PINS_3[i], data[number+1][i])

time.sleep(5)
print('PIR Ready...')

try:
    while True:
        val = GPIO.input(PIR_PIN) # PIR 센서의 입력값을 val에 저장

        if val:
            if stopwatch == 100: # 10초 동안 움직임이 계속 감지되면 위험 경보를 울림
                for i in range(0, 2): # 0.05초 간격으로 2번씩 반복(계속 움직임이 감지될 경우 반복)
                    GPIO.output(BUZ_PIN, True)
                    time.sleep(0.05)
                    GPIO.output(BUZ_PIN, False) 
            else:
                if stopwatch >= 50: # 5초 동안 움직임이 계속 감지되면 노란색 OFF 빨간색 ON
                    GPIO.output(LED_YEL, GPIO.LOW)
                    GPIO.output(LED_RED, GPIO.HIGH)

                    stopwatch += 1 # 0.1초 증가
                else:
                    GPIO.output(LED_RED, GPIO.LOW) # 움직임이 감지되면 초록색 OFF 노란색 ON
                    GPIO.output(LED_GRE, GPIO.LOW)
                    GPIO.output(LED_YEL, GPIO.HIGH) 

                    stopwatch += 1 # 0.1초 증가

        else: 
            GPIO.output(LED_RED, GPIO.LOW) # 움직임이 없을 때는 초록색 ON
            GPIO.output(LED_YEL, GPIO.LOW)
            GPIO.output(LED_GRE, GPIO.HIGH) 

            stopwatch = 0 # 중간에 움직임이 멈추면 초기화

                    
        display1(int(stopwatch/100))     # 10초대
        display2(int(stopwatch%100/10))  # 1초대
        display3(int(stopwatch%10))      # 0.1초대
        # print(stopwatch)

        time.sleep(0.1) # 0.1초 간격 유지

finally:
    GPIO.setup(PIR_PIN, GPIO.IN)
    GPIO.setup(BUZ_PIN, GPIO.IN)
    GPIO.setup(LED_RED, GPIO.IN)
    GPIO.setup(LED_YEL, GPIO.IN)
    GPIO.setup(LED_GRE, GPIO.IN)
    GPIO.cleanup()
    print('cleanup and exit')