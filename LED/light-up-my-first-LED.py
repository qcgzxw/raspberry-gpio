import RPi.GPIO as GPIO
import time

# define LED PIN
PIN_LIGHT_BLUE1 = 11
PIN_LIGHT_BLUE2 = 12
PIN_LIGHT_GREEN1 = 13
PIN_LIGHT_GREEN2 = 15

LED_STATUS_OFF = 0
LED_STATUS_ON = 1

TIME_INTERVAL = 0.1

MAX_CYCLE_TIMES = 100

LIGHT_LIST = [PIN_LIGHT_BLUE1, PIN_LIGHT_BLUE2, PIN_LIGHT_GREEN1, PIN_LIGHT_GREEN2]

# init
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_LIGHT_BLUE1, GPIO.OUT)
    GPIO.setup(PIN_LIGHT_BLUE2, GPIO.OUT)
    GPIO.setup(PIN_LIGHT_GREEN1, GPIO.OUT)
    GPIO.setup(PIN_LIGHT_GREEN2, GPIO.OUT)


def destroy():
    print('Light Over!')
    GPIO.cleanup()


def switchLight(light, status):
    if not light in LIGHT_LIST:
        return
    if status == LED_STATUS_OFF:
        print("Light " + str(light) + " switch to off.")
        GPIO.output(light, GPIO.LOW)
    elif status == LED_STATUS_ON:
        print("Light " + str(light) + " switch to on.")
        GPIO.output(light, GPIO.HIGH)

def paomadeng():
    try:
        i = 0
        while True:
            if i > MAX_CYCLE_TIMES:
                break
            for light in LIGHT_LIST:
                switchLight(light, LED_STATUS_ON)
                time.sleep(TIME_INTERVAL)
            for light in LIGHT_LIST:
                switchLight(light, LED_STATUS_OFF)
                time.sleep(TIME_INTERVAL)
            i += 1
    finally:
        destroy()

def test():
    try:
        i = 0
        while True:
            if i > 10:
                break
            GPIO.output(PIN_LIGHT_GREEN2, True)
            time.sleep(TIME_INTERVAL)
            GPIO.output(PIN_LIGHT_GREEN2, False)
            time.sleep(TIME_INTERVAL)
            i += 1
    finally:
        GPIO.cleanup()

# main
init()
#test()
paomadeng()
