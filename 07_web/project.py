from flask import Flask, render_template, Response
import RPi.GPIO as GPIO
import Adafruit_DHT
from camera import Camera # pi카메라를 이용한 카메라 파이썬 파일 불러오기
import spidev
import time

# adafruit 모듈을 sensor로 받기
sensor = Adafruit_DHT.DHT11

# 온습도 모듈 센서 GPIO PIN 번호
tem_hum_PIN = 23

# LED GPIO PIN 번호
LED_RED = 17
LED_YELLOW = 27
LED_GREEN = 22

# SPI 통신 설정
spi = spidev.SpiDev()
spi.open(0, 0) # 0번 : 토양수분센서
spi.open(0, 1) # 1번 : 조도센서
spi.max_speed_hz = 100000

app = Flask(__name__)

# LED GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_YELLOW, GPIO.OUT)

# 채널 별 SPI 값 받아올 수 있는 함수
def analog_read(channel): 
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

# 카메라 프레임 받아오기
def camera(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route("/monitor")
def monitoring():
    return Response(camera(Camera()),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

# 온습도, 토양수분, 조도 값 받아오기
@app.route("/")
def get_data():
    # Adafruit을 이용해서 온습도 받아오기
    h, t = Adafruit_DHT.read_retry(sensor, tem_hum_PIN)
    
    # analog_read 함수를 이용하여 channel 0번에서 토양수분 값 받아오기(퍼센트 값으로 나타내기 위한 식)
    soil = analog_read(0)
    
    # 토양수분 값이 500미만일 때(수분 충분) 파란색 LED ON, 빨간색 · 노란색 LED OFF
    if soil < 500:
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.HIGH)

    # 토양수분 값이 500 이상 900 미만(수분 위험)일 때 노란색 LED ON, 빨간색 · 파란색 LED OFF
    elif 500 <= soil < 900: 
        GPIO.output(LED_RED, GPIO.LOW)
        GPIO.output(LED_YELLOW, GPIO.HIGH)
        GPIO.output(LED_GREEN, GPIO.LOW)
        time.sleep(1)

    # 토양수분 값이 900 이상(수분 부족) 일 때 빨간색 LED ON, 노란색 · 파란색 LED OFF
    else:
        GPIO.output(LED_RED, GPIO.HIGH)
        GPIO.output(LED_YELLOW, GPIO.LOW)
        GPIO.output(LED_GREEN, GPIO.LOW)

    soil_value = (1024-soil)/10

    # analog_read 함수를 이용하여 channel 1번에서 조도 값 받아오기
    light_value = analog_read(1)
    
    # 온도, 습도 값을 받아오는데 문제가 없을 경우
    if h is not None and t is not None:
        # main.html에 온도, 습도, 토양수분, 조도 값 넘기기
        return render_template("main.html", hum=h, tem=t, soil=soil_value, light=light_value)
    else:
        # 오류가 있을 경우, 'Read error' 출력
        return 'Read error'
        

if __name__ == "__main__":
    try: 
        app.run(host="0.0.0.0", debug=True, threaded=True)
    finally:
        GPIO.cleanup()
        spi.close()
