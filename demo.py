# general imports
import numpy as np
import math
import time


import os, sys
import RPi.GPIO as GPIO

# for gps
# import serial
# # written agribots files
# import encoders as enc
# from motors import DriveMode
# import motors as mot
# import imu
# import gps
# import path_planner as path
# from mpu9250_i2c import *
# for raspi

# uses dependencies like GPIO that cannot be tested easily
# has the master pinout of raspi

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


def read_vals():
    global ang_vel_desired
    f = open('actions.txt', 'r')
    lines = f.read().split('\n')
    # print(lines)
    # lines = lines[0:min(2,len(lines))]
    try:
        for i, line in enumerate(lines):
            if i == 0:
                ang_vel_desired[0] = float(line)
                ang_vel_desired[2] = float(line)

            elif i == 1:
                ang_vel_desired[1] = float(line)
                ang_vel_desired[3] = float(line)
    except:
        print('cannot_read')


if __name__ == "__main__":
    init_pins()
