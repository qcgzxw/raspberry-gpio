import RPi.GPIO as GPIO
import time

DJ_UD = 17
DJ_LR = 18

FREQUENCY = 50
DC_0 = 2.5
DC_90 = 7.5
DC_180 = 12.5

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DJ_UD, GPIO.OUT)
    GPIO.setup(DJ_LR, GPIO.OUT)

def destroy():
    print('SG90 test over!')
    GPIO.cleanup()

def DJ_test():
    dj_ud = GPIO.PWM(DJ_UD, FREQUENCY)
    dj_ud.start(DC_90)
    print('dj_ud start')
    time.sleep(1)
    dj_lr = GPIO.PWM(DJ_LR, FREQUENCY)
    dj_lr.start(DC_90)
    print('dj_lr start')
    i = 1
    for i in range(1, 5):
        dj_ud.ChangeDutyCycle(DC_0)
        print('dj_ud turn to 0')
        time.sleep(0.5)
        dj_ud.ChangeDutyCycle(DC_180)
        print('dj_ud turn to 180')
        dj_lr.ChangeDutyCycle(DC_0)
        print('dj_lr turn to 0')
        time.sleep(0.5)
        dj_lr.ChangeDutyCycle(DC_180)
        print('dj_lr turn to 180')
        i += 1
    time.sleep(1)
    dj_ud.ChangeDutyCycle(DC_90)
    dj_lr.ChangeDutyCycle(DC_90)
    time.sleep(1)
    dj_ud.stop()
    dj_lr.stop()


init()
DJ_test()
time.sleep(5)
destroy()

