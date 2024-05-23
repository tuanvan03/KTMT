# 3.Viết chương trình thực hiện chức năng, khi đèn LED sáng thì đèn nền màn hình LCD tắt, ngược lại đèn LED tắt thì đèn nền màn hình LCD sáng.
# Quá trình này lặp đi lặp lại theo chu kỳ 1s
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 13
GPIO.setup(LED, GPIO.OUT)
BL = 12
GPIO.setup(BL, GPIO.OUT)


def led_bl():
    GPIO.output(LED, not GPIO.input(LED))
    GPIO.output(BL, not GPIO.input(BL))


try:
    led_bl()
    time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
