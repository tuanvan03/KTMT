# 6.Viết chương trình
# bấm button 1 đèn LED sáng,
# bấm button 2 đèn LED tắt,
# bấm button 3 đèn LED nhấp nháy theo chu kỳ 1s,
# bấm button 4 lần 1 đèn LED sáng, lần 2 đèn LED tắt.
# Hiển thị trạng thái các phím đã bấm lên terminal.
import RPi.GPIO as GPIO
import time
from multiprocessing import Value, Process

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LED = 13
BT1 = 21
BT2 = 26
BT3 = 20
BT4 = 19

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BT1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BT2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BT3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BT4, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def handle_BT1(press_BT3, press_BT4):
    while True:
        if GPIO.input(BT1) == GPIO.LOW:
            print("Pressed  BT1")
            press_BT3.value = False
            press_BT4.value = 0
            GPIO.output(LED, GPIO.HIGH)
        time.sleep(0.15)


def handle_BT2(press_BT3, press_BT4):
    while True:
        if GPIO.input(BT2) == GPIO.LOW:
            print("Pressed  BT2")
            press_BT3.value = False
            press_BT4.value = 0
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.15)


def handle_BT3(press_BT3, press_BT4):
    while True:
        if GPIO.input(BT3) == GPIO.LOW:
            print("Pressed  BT3")
            press_BT3.value = True
            press_BT4.value = 0

        if press_BT3.value:
            GPIO.output(LED, not GPIO.input(LED))
            time.sleep(1)
        time.sleep(0.15)


def handle_BT4(press_BT3, press_BT4):
    while True:
        if GPIO.input(BT4) == GPIO.LOW:
            print("Pressed  BT4")
            press_BT3.value = False
            press_BT4.value = (press_BT4.value % 2) + 1

        if press_BT4.value == 1:
            GPIO.output(LED, GPIO.HIGH)
        else:
            GPIO.output(LED, GPIO.LOW)
        time.sleep(0.15)


def main():
    press_BT4 = Value("d", 0)  # bien dung chung giua cac tien trinh kieu double
    press_BT3 = Value("i", False)  # bien dung chung giua cac tien trinh kieu integer
    Process(target=handle_BT1, args=(press_BT3, press_BT4)).start()
    Process(target=handle_BT2, args=(press_BT3, press_BT4)).start()
    Process(target=handle_BT3, args=(press_BT3, press_BT4)).start()
    Process(target=handle_BT4, args=(press_BT3, press_BT4)).start()


try:
    main()
except KeyboardInterrupt:
    GPIO.cleanup
