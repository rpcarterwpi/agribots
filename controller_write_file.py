import time
import math
from enum import IntEnum
from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
# from TankDrive import DriveMode, Motors, tank_drive

class DriveMode(IntEnum):
    DRIVE = 1
    BRAKE = 2
    COAST = 3

MAX_SPEED = 100

cur_effort_L = 0
cur_effort_R = 0
cur_drivemode_L = DriveMode.COAST
cur_drivemode_R = DriveMode.COAST

def write_vals():
    f = open('actions.txt', 'w')
    # print(cur_effort_L)
    # print(cur_effort_R)
    # print(cur_drivemode_L)
    # print(cur_drivemode_L)
    f.write(str(cur_effort_L)+'\n')
    f.write(str(cur_effort_R)+'\n')
    f.write(str(int(cur_drivemode_L))+'\n')
    f.write(str(int(cur_drivemode_R))+'\n')
    f.close()

# while True:
#     time.sleep(0.1)
#     cur_effort_L += 0.01
#     cur_effort_R -= 0.01
#     if time.time()%2==0:
#         cur_drivemode_L = DriveMode.DRIVE
#         cur_drivemode_R = DriveMode.DRIVE
#     else:
#         cur_drivemode_L = DriveMode.BRAKE
#         cur_drivemode_R = DriveMode.BRAKE
#     write_vals()
#
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
        # print(f'L Forward: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.LEFT)
        cur_drivemode_L = DriveMode.DRIVE
        cur_effort_L = effort
        print(cur_effort_L)
        write_vals()

    def on_L3_down(self,value):
        effort = -1*MAX_SPEED*normalize_joystick(False,value)
        # print(f'L Back: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.LEFT)
        cur_drivemode_L = DriveMode.DRIVE
        cur_effort_L = effort
        print(cur_effort_L)
        write_vals()

    def on_L3_y_at_rest(self):
        # print('L Coast')
        # tank_drive(DriveMode.COAST,0,Motors.LEFT)
        cur_drivemode_L = DriveMode.COAST
        cur_effort_L = 0
        print(cur_effort_L)
        write_vals()

    def on_R3_up(self,value):
        effort = MAX_SPEED*normalize_joystick(True,value)
        # print(f'R Forward: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.RIGHT)
        cur_drivemode_R = DriveMode.DRIVE
        cur_effort_R = effort
        print(cur_effort_R)
        write_vals()

    def on_R3_down(self,value):
        effort = -1*MAX_SPEED*normalize_joystick(False,value)
        # print(f'R Back: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.RIGHT)
        cur_drivemode_R = DriveMode.DRIVE
        cur_effort_R = effort
        print(cur_effort_R)
        write_vals()

    def on_R3_y_at_rest(self):
        # print('R Coast')
        # tank_drive(DriveMode.COAST,0,Motors.RIGHT)
        cur_drivemode_R = DriveMode.COAST
        cur_effort_R = 0
        print(cur_effort_R)
        write_vals()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()
