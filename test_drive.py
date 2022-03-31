from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
import time
import math
from enum import Enum

class DriveMode(Enum):
    DRIVE = 1
    BRAKE = 2
    COAST = 3
#
# class Motors(Enum):
#     LEFT = 1
#     RIGHT = 2
#     PUMP = 3
#
# # SetMode
# GPIO.setmode(GPIO.BOARD)
#
# # Left Setup
# ENA1, IN1, IN2 = 33, 29, 31
# GPIO.setup(ENA1, GPIO.OUT)
# GPIO.setup(IN1, GPIO.OUT)
# GPIO.setup(IN2, GPIO.OUT)
#
# # Right Setup
# ENA2, IN3, IN4 = 32, 16, 18
# GPIO.setup(ENA2, GPIO.OUT)
# GPIO.setup(IN3, GPIO.OUT)
# GPIO.setup(IN4, GPIO.OUT)
#
# PWM_FREQ = 100
MAX_SPEED = 100

cur_effort_L = 0
cur_effort_R = 0
cur_drivemode_L = DriveMode.COAST
cur_drivemode_R = DriveMode.COAST

def write_vals():
    f = open('actions.txt', 'w')
    f.write(str(cur_effort_L))
    f.write(str(cur_effort_R))
    f.write(str(cur_drivemode_L))
    f.write(str(cur_drivemode_R))
    f.close()


# def tank_drive(mode,effort,motor):
#     if motor == Motors.LEFT:
#         print('left')
#         ENA = ENA1
#         INA = IN1
#         INB = IN2
#     elif motor == Motors.RIGHT:
#         print('right')
#         ENA = ENA2
#         INA = IN3
#         INB = IN4
#     print(ENA)
#     print(INA)
#     print(INB)
#     if mode == DriveMode.DRIVE:
#         print('drive')
#         if effort != 0:
#             forward = effort/abs(effort) >= 0
#             print(forward)
#             if forward:
#                 print('forward')
#                 GPIO.output(INA, GPIO.HIGH)
#                 GPIO.output(INB, GPIO.LOW)
#             else:
#                 GPIO.output(INA, GPIO.LOW)
#                 GPIO.output(INB, GPIO.HIGH)
#
#     elif mode == DriveMode.BRAKE:
#         GPIO.output(INA, GPIO.LOW)
#         GPIO.output(INB, GPIO.LOW)
#
#     elif mode == DriveMode.COAST:
#         GPIO.output(INA, GPIO.HIGH)
#         GPIO.output(INB, GPIO.HIGH)
#
#     PWM_cur = GPIO.PWM(ENA,PWM_FREQ)
#     PWM_cur.start(abs(effort))
#     print(abs(effort))
#     print('going to pwm')



def normalize_joystick(dir_up,value):
    if dir_up:
        new_value = max(0.0,min(1.0,abs((value+281)/-32486)))
    else:
        new_value = max(0.0,min(1.0,abs((value-281)/32486)))
    return new_value

class MyController(Controller):
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_up(self,value):
        effort = MAX_SPEED*normalize_joystick(True,value)
        print(f'L Forward: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.LEFT)
        cur_drivemode_L = DriveMode.DRIVE
        cur_effort_L = effort
        write_vals()

    def on_L3_down(self,value):
        effort = -1*MAX_SPEED*normalize_joystick(False,value)
        print(f'L Back: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.LEFT)
        cur_drivemode_L = DriveMode.DRIVE
        cur_effort_L = effort
        write_vals()

    def on_L3_y_at_rest(self):
        print('L Coast')
        # tank_drive(DriveMode.COAST,0,Motors.LEFT)
        cur_drivemode_L = DriveMode.COAST
        cur_effort_L = 0
        write_vals()

    def on_R3_up(self,value):
        effort = MAX_SPEED*normalize_joystick(True,value)
        print(f'R Forward: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.RIGHT)
        cur_drivemode_R = DriveMode.DRIVE
        cur_effort_R = effort
        write_vals()

    def on_R3_down(self,value):
        effort = -1*MAX_SPEED*normalize_joystick(False,value)
        print(f'R Back: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.RIGHT)
        cur_drivemode_R = DriveMode.DRIVE
        cur_effort_R = effort
        write_vals()

    def on_R3_y_at_rest(self):
        print('R Coast')
        tank_drive(DriveMode.COAST,0,Motors.RIGHT)
        cur_drivemode_R = DriveMode.COAST
        cur_effort_R = 0
        write_vals()

# Create Controller
# controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
# controller.listen()

# tank_drive(DriveMode.DRIVE,100,Motors.LEFT)
# tank_drive(DriveMode.DRIVE,100,Motors.RIGHT)


# cur_effort_L = 0
# cur_effort_R = 0
# cur_drivemode_L = DriveMode.COAST
# cur_drivemode_R = DriveMode.COAST

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()


# tank_drive(cur_drivemode_L,cur_effort_L,Motors.LEFT)
# tank_drive(cur_drivemode_R,cur_effort_R,Motors.LEFT)

# GPIO.output(IN1, GPIO.HIGH)
# GPIO.output(IN2, GPIO.LOW)
#
# PWM_cur = GPIO.PWM(ENA1,PWM_FREQ)
# PWM_cur.start(100)
# drive()


# GPIO.cleanup()
