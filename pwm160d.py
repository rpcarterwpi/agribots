# Imported Libraries
import RPi.GPIO as GPIO
from time import sleep

# SetMode
GPIO.setmode(GPIO.BOARD)

# Motor 1 Setup
ENA1, IN1, IN2 = 33, 29, 31
GPIO.setup(ENA1, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
# 
# PWMA = GPIO.PWM(ENA1, 50)
# PWMA.start(50)

GPIO.output(IN1, GPIO.HIGH)
GPIO.output(ENA1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

sleep(2.5)
GPIO.cleanup()
