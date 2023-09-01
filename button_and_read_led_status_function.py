import RPi.GPIO as GPIO
import time

LED_PIN_LIST = [17, 27, 22]
BUTTON_PIN = 26

def led_on(led_index):
    GPIO.output(LED_PIN_LIST[led_index], GPIO.HIGH)
    
def led_off(led_index):
    GPIO.output(LED_PIN_LIST[led_index], GPIO.LOW)
    
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_LIST[0], GPIO.OUT)
GPIO.setup(LED_PIN_LIST[1], GPIO.OUT)
GPIO.setup(LED_PIN_LIST[2], GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN)

GPIO.output(LED_PIN_LIST[0], GPIO.LOW)
GPIO.output(LED_PIN_LIST[1], GPIO.LOW)
GPIO.output(LED_PIN_LIST[2], GPIO.LOW)

previous_button_state = GPIO.input(BUTTON_PIN)
led_index = 0

while True:
    time.sleep(0.01)
    button_state = GPIO.input(BUTTON_PIN)
    if button_state != previous_button_state:
        previous_button_state = button_state
        if button_state == GPIO.HIGH:
            if led_index == 0:
                # power on LED 0
                led_on(led_index)
                led_off(led_index + 1)
                led_off(led_index + 2)                
                led_index = 1
            elif led_index == 1:
                # power on LED 1
                led_off(led_index - 1)
                led_on(led_index)
                led_off(led_index + 1)
                led_index = 2
            else:
                # power on LED 2
                led_off(led_index - 2)
                led_off(led_index - 1)
                led_on(led_index)
                led_index = 0                
                
GPIO.cleanup()


