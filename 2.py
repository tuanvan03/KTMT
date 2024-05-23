# 2.Viết chương trình thực hiện chức năng, đèn LED sáng 1s, tắt 2s, sáng 3s, tắt 1s lặp đi lặp lại quá trình này.
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 13
GPIO.setup(LED, GPIO.OUT)


def led(state, t):
    GPIO.output(LED, state)
    time.sleep(t)


try:
    led(GPIO.HIGH, 1)
    led(GPIO.LOW, 2)
    led(GPIO.HIGH, 3)
    led(GPIO.LOW, 1)

except KeyboardInterrupt:
    GPIO.cleanup()
