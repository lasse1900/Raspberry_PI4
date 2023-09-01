import RPi.GPIO as GPIO
import time

LED_PIN_LIST = [17, 27, 22, 19]
BUTTON_PIN = 26

def led_on(led_index):
    if led_index not in LED_PIN_LIST:
        return
    for pin in LED_PIN_LIST:
        if pin == led_index:
            GPIO.output(pin, GPIO.HIGH)
        else:
            GPIO.output(pin, GPIO.LOW)            
                
GPIO.setmode(GPIO.BCM)
for pin in LED_PIN_LIST:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)


previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0

while True:
    time.sleep(0.01)
    button_state = GPIO.input(BUTTON_PIN)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            led_on(LED_PIN_LIST[led_index])
            led_index += 1
            if led_index >= len(LED_PIN_LIST):
                led_index = 0
             
                
GPIO.cleanup()



