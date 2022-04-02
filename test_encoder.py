import RPi.GPIO as GPIO
import time
import math

# SetMode
GPIO.setmode(GPIO.BOARD)
ENC1 = 22
GPIO.setup(ENC1, GPIO.IN)

while True:
    print(GPIO.input(ENC1))
    time.sleep(0.1)
