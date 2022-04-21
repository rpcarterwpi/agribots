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

arduino_pin1 = 33

pwm_freq = 100
read_args = [0,0]

IN_forward = np.array([1,0])
IN_back = np.array([0,1])

motors_min_effort = 0
motors_max_effort = 100

def init_pins():
    GPIO.setmode(GPIO.BOARD)
    for pin in IN_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in PWM_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in enc_pins:
        GPIO.setup(pin, GPIO.IN)
    GPIO.setup(arduino_pin1, GPIO.OUT)

def control_drive(efforts):
    IN_write = np.zeros(4)
    PWM_write = np.zeros(4)

    IN_write[0:2] = IN_forward if efforts[0] >= 0 else IN_back
    IN_write[2:4] = IN_forward if efforts[1] >= 0 else IN_back

    PWM_write = np.clip(np.rint(np.abs(efforts)),motors_min_effort,motors_max_effort)
    return ((IN_write, PWM_write))

def motors_write_raw(motors_write):
    IN_write, PWM_write = motors_write
    for i, in_pin in enumerate(IN_pins):
        GPIO.output(in_pin, GPIO.HIGH if IN_write[i] == 1 else GPIO.LOW)
    for i, pwm_pin in enumerate(PWM_pins):
        if PWM_write[i] < 20:
            PWM_write[i] = 0
        PWM_cur = GPIO.PWM(pwm_pin,pwm_freq)
        PWM_cur.start(PWM_write[i])
        time.sleep(1/pwm_freq)


def read_vals():
    f = open('actions.txt', 'r')
    str = f.read()
    pass_args = str.split(',')

    for i, arg in enumerate(pass_args):
        if arg != '':
            read_args[i] = float(arg)
    f.close()
            #
            # print(arg)
            # try:
            #
            # except:
            #     print('cannot read')
            #     # time.sleep(1/pwm_freq)
            #     read_args = [0,0]
    # except:
    #     print('cannot_read')
    #     time.sleep(10/pwm_freq)
    #

def write_arduino(on_val):
    if on_val:
        GPIO.output(arduino_pin1, GPIO.HIGH)
    else:
        GPIO.output(arduino_pin1, GPIO.LOW)



if __name__ == "__main__":
    init_pins()

    while True:
        try:
            # read_vals()
            # efforts = 100 * np.array([read_args[0],read_args[1],read_args[0],read_args[1]])
            # motors_write = control_drive(efforts)
            # motors_write_raw(motors_write)

            write_arduino(True)
            print(writing)
            time.sleep(1)


            # print(read_args)

        except KeyboardInterrupt:
            print(': interupted, cleaning up')
            break
