# 5.Viết chương trình bấm button 1 lần 1 đèn LED sáng, bấm button 1 lần 2 thì đèn LED tắt, quá trình này lặp đi lặp lại.

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 13
GPIO.setup(LED, GPIO.OUT)
BT1 = 21
GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
state = False


def led():
    if GPIO.input(BT1) == GPIO.LOW:
        state = not state
        GPIO.output(LED, state)
        time.sleep(0.25)


try:
    while True:
        led()
except KeyboardInterrupt:
    GPIO.cleanup()
