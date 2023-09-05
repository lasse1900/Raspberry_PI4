 
# Example usage http://192.168.10.53:8500/led/17/state/1
from flask import Flask
import RPi.GPIO as GPIO

BUTTON_PIN = 26
LED_PIN_LIST = [17, 27, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN)
for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
app = Flask(__name__)

for pin in LED_PIN_LIST:
    GPIO.output(pin, GPIO.LOW)

@app.route("/")
def index():
    return "Hello from Flask"


@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        return "Button is pressed"
    return "Button is NOT pressed"



@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    led_status = "OFF"
    if not led_pin in LED_PIN_LIST:
        return "Wrong GPIO number: " + str(led_pin)
    if led_state == 0:
        GPIO.output(led_pin, GPIO.LOW)
        led_status = "OFF"
    elif led_state == 1:
        GPIO.output(led_pin, GPIO.HIGH)
        led_status = "ON"
    else:
        return "State must be 0 or 1"
    print("led_status: ", led_status)
    result = f"The value of the LED# {led_pin} is: {led_status}"
    return result

    
app.run(host="0.0.0.0", port=8500)
