import RPi.GPIO as GPIO
import time

LED_PIN = 17
BUTTON_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

# At start LED is OFF
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.setmode(GPIO.BCM)


while True:
    time.sleep(0.5)
    state = GPIO.input(BUTTON_PIN)
    print(state)

    if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        
GPIO.cleanup()
        
    
