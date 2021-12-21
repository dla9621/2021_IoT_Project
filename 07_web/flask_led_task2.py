from flask import Flask, render_template
import RPi.GPIO as GPIO

RED_LED_PIN = 4
BLUE_LED_PIN= 17

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

@app.route("/")
def home():
    return render_template("led2.html", title="LED ON/OFF")

@app.route("/led/<color>/<op>")
def led_color_op(color, op):
    if color == "red":
        if op == "on":
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return "RED LED ON"
        elif op == "off":
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return "RED LED OFF"
    elif color == "blue":
        if op == "on":
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
            return "BLUE LED ON"
        elif op == "off":
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)
            return "BLUE LED OFF"

if __name__ == "__main__":
    try: 
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
