import numpy as np
import math
import time

# uses dependencies like GPIO that cannot be tested easily
# has the master pinout of raspi

pin_enc_RL, pin_enc_FL, pin_enc_RR, pin_enc_FR = 16, 18, 11, 13

pin_motor_RL, pin_motor_FL, pin_motor_RR, pin_motor_FR = 37, 35, 31, 29
pin_IN1, pin_IN2, pin_IN3, pin_IN4 = 22, 24, 26, 36

def encoder_read_raw():
    return np.array([GPIO.input(enc_FL),GPIO.input(enc_FR),GPIO.input(enc_RL),GPIO.input(enc_RR)])

def gps_read_raw():
    pass

def imu_read_raw():
    pass

def motors_write_raw():
    pass
