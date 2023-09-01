import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_PIN, GPIO.OUT)

# At start LED is OFF
GPIO.output(LED_PIN, GPIO.LOW)

state = int(input("Give me the input to the LED ON/OFF == 0/1: "))

if state == 1:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(3)
if state == 0:
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
else:
    GPIO.cleanup()
    exit
    
print("The END")
