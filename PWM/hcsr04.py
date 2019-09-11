import RPi.GPIO as GPIO
import time

TRIG_PIN = 20
ECHO_PIN = 21

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT, initial = GPIO.LOW)
    GPIO.setup(ECHO_PIN, GPIO.IN)


def checkdist():
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(TRIG_PIN, GPIO.LOW)
    while not GPIO.input(ECHO_PIN):
        pass
    t1 = time.time()
    while GPIO.input(ECHO_PIN):
        pass
    t2 = time.time()
    return (t2 - t1) * 340 * 100 / 2


def destroy():
    print('HC-SR04 Test Over.')
    GPIO.cleanup()

def test():
    try:
        while True:
            print('Distance: %2f cm' % checkdist())
            time.sleep(0.5)
    except KeyboardInterrupt:
        destroy()
        return

init()
test()
