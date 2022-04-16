# general imports
import numpy as np
import math
import time


import os, sys
import RPi.GPIO as GPIO

# encoder pins
pin_enc_RL, pin_enc_FL, pin_enc_RR, pin_enc_FR = 16, 18, 11, 13
enc_pins = [pin_enc_FL, pin_enc_FR, pin_enc_RL, pin_enc_RR]
# pwm pins
pin_motor_RL, pin_motor_FL, pin_motor_RR, pin_motor_FR = 37, 35, 31, 29
PWM_pins = [pin_motor_FL, pin_motor_FR, pin_motor_RL, pin_motor_RR]
# direction pins
pin_IN1, pin_IN2, pin_IN3, pin_IN4 = 22, 24, 26, 36
IN_pins = [pin_IN1, pin_IN2, pin_IN3, pin_IN4]

pwm_freq = 100

def init_pins():
    GPIO.setmode(GPIO.BOARD)
    for pin in IN_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in PWM_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in enc_pins:
        GPIO.setup(pin, GPIO.IN)

read_args = [1,1]

def read_vals():
    f = open('actions.txt', 'r')
    str = f.read()
    print(str)
    pass_args = str.split(',')
    try:
        for i, arg in enumerate(pass_args):
            read_args[i] = arg
    except:
        print('cannot_read')


if __name__ == "__main__":
    init_pins()
    read_vals()
