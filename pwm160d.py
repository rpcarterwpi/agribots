# Imported Libraries
import RPi.GPIO as GPIO
from time import sleep

# SetMode
GPIO.setmode(GPIO.BOARD)

# Motor 1 Setup
PWR1, ENA1, IN1, IN2, GND = 2, 33, 31, 29, 39
GPIO.setup(ENA1, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
PWMA = GPIO.PWM(ENA1, 50)
PWMA.start(0)
sleep(2.5)
