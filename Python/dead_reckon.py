import time
import math
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
    if motor == Motors.LEFT:
        # print('left')
        ENA = ENA1
        INA = IN1
        INB = IN2
    elif motor == Motors.RIGHT:
        # print('right')
        ENA = ENA2
        INA = IN3
        INB = IN4
    print(ENA)
    print(INA)
    print(INB)
    if mode == DriveMode.DRIVE:
        print('drive')
        if effort != 0:
            forward = effort/abs(effort) >= 0
            print(forward)
            if forward:
                print('forward')
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

# SetMode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA1, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

end_time = time.time() + 5
while time.time() < end_time:
    try:
        tank_drive(DriveMode.DRIVE,-100,Motors.RIGHT)
        tank_drive(DriveMode.DRIVE,100,Motors.LEFT)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
end_time = time.time() + 5
while time.time() < end_time:
    try:
        tank_drive(DriveMode.DRIVE,100,Motors.RIGHT)
        tank_drive(DriveMode.DRIVE,-100,Motors.LEFT)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break

GPIO.cleanup()
