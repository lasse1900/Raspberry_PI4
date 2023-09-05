from flask import Flask
import RPi.GPIO as GPIO

BUTTON_BIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_BIN, GPIO.IN)
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Flask"

@app.route("/push-btton")
def check_push_button_state():
    if GPIO.input(BUTTON_BIN) == GPIO.HIGH:
        return "Button is pressed"
    return "Button is NOT pressed"
    
    
app.run(host="0.0.0.0", port=8500)


