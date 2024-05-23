# 4.Viết chương trình bấm button 1 thì đèn LED sáng, thả button 1 thì đèn LED tắt.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 13
GPIO.setup(LED, GPIO.OUT)
BT1 = 21
GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def updateLed():
    if GPIO.input(BT1) == GPIO.LOW:
        GPIO.output(LED, GPIO.HIGH)
    else:
        GPIO.output(LED, GPIO.LOW)


try:
    while True:
        updateLed()
except KeyboardInterrupt:
    GPIO.cleanup()
