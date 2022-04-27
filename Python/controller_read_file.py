import time
import math
from enum import IntEnum

import RPi.GPIO as GPIO
from enum import IntEnum

class DriveMode(IntEnum):
    DRIVE = 1
    BRAKE = 2
    COAST = 3

class Motors(IntEnum):
    LEFT = 1
    RIGHT = 2

# Left Setup
ENA1, IN1, IN2 = 33, 29, 31

# Right Setup
ENA2, IN3, IN4 = 32, 16, 18

PWM_FREQ = 100
MAX_SPEED = 100

def tank_drive(mode,effort,motor):
    if motor == Motors.RIGHT:
        # print('left')
        ENA = ENA1
        INA = IN1
        INB = IN2
    elif motor == Motors.LEFT:
        # print('right')
        ENA = ENA2
        INA = IN3
        INB = IN4
    # print(ENA)
    # print(INA)
    # print(INB)
    if mode == DriveMode.DRIVE:
        # print('drive')
        if effort != 0:
            forward = effort/abs(effort) >= 0
            # print(forward)
            if forward:
                # print('forward')
                GPIO.output(INA, GPIO.HIGH)
                GPIO.output(INB, GPIO.LOW)
            else:
                GPIO.output(INA, GPIO.LOW)
                GPIO.output(INB, GPIO.HIGH)

    elif mode == DriveMode.BRAKE:
        GPIO.output(INA, GPIO.LOW)
        GPIO.output(INB, GPIO.LOW)

    elif mode == DriveMode.COAST:
        GPIO.output(INA, GPIO.HIGH)
        GPIO.output(INB, GPIO.HIGH)

    PWM_cur = GPIO.PWM(ENA,PWM_FREQ)
    PWM_cur.start(abs(effort))
    # print(abs(effort))
    print('going to pwm')

drive_vals = [0,0,DriveMode.COAST,DriveMode.COAST]

def read_vals():
    f = open('actions.txt', 'r')
    lines = f.read().split('\n')
    lines = lines[0:min(4,len(lines))]
    for i, line in enumerate(lines):
        try:
            if i == 2 or i == 3:
                drive_vals[i] = DriveMode(int(line))
            else:
                drive_vals[i] = int(round(float(line)))
        except:
            print('tryingagain')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA1, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

while True:
    try:
        read_vals()
        print(drive_vals)
        tank_drive(drive_vals[2],drive_vals[0],Motors.LEFT)
        tank_drive(drive_vals[3],drive_vals[1],Motors.RIGHT)

    except KeyboardInterrupt:
        print('cleaningup')
        GPIO.cleanup()
        break
