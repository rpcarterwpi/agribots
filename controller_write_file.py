import time
import math
# from enum import IntEnum
from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO
# from TankDrive import DriveMode, Motors, tank_drive

# class DriveMode(IntEnum):
#     DRIVE = 1
#     BRAKE = 2
#     COAST = 3

MAX_SPEED = 2.2





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
        self.cur_effort_L = 0
        self.cur_effort_R = 0
        # self.cur_drivemode_L = DriveMode.COAST
        # self.cur_drivemode_R = DriveMode.COAST

    def write_vals(self):
        f = open('actions.txt', 'w')
        f.write(str(self.cur_effort_L)+'\n')
        f.write(str(self.cur_effort_R))

        # f.write(str(self.cur_effort_L)+'\n')
        # f.write(str(self.cur_effort_R)+'\n')
        # f.write(str(int(self.cur_drivemode_L))+'\n')
        # f.write(str(int(self.cur_drivemode_R))+'\n')
        # print(self.cur_effort_L)
        # print(self.cur_effort_R)
        # print(self.cur_drivemode_L)
        # print(self.cur_drivemode_L)
        f.close()

    def on_L3_up(self,value):
        effort = MAX_SPEED*normalize_joystick(True,value)
        # print(f'L Forward: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.LEFT)
        # self.cur_drivemode_L = DriveMode.DRIVE
        self.cur_effort_L = effort
        print(self.cur_effort_L)
        self.write_vals()

    def on_R2_press(self,value):
        new_val = (value * -1 + 281)/32486
        # new_value = max(0.0,min(1.0,abs((value+281)/-32486)))
        print(new_val)
        # effort = MAX_SPEED*normalize_joystick(True,value)
        # self.cur_effort_R = effort
        # print(self.cur_effort_R)
        self.write_vals()

    def on_L2_press(self,value):
        a = 1
        # print(value)
        # effort = MAX_SPEED*normalize_joystick(True,value)
        # self.cur_effort_R = effort
        # print(self.cur_effort_R)
        # self.write_vals()



    def on_L3_right(self,value):
        a = 1

    def on_L3_left(self,value):
        a = 1

    def on_R3_right(self,value):
        a = 1

    def on_R3_left(self,value):
        a = 1

    def on_L3_down(self,value):
        effort = -1*MAX_SPEED*normalize_joystick(False,value)
        # print(f'L Back: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.LEFT)
        # self.cur_drivemode_L = DriveMode.DRIVE
        self.cur_effort_L = effort
        print(self.cur_effort_L)
        self.write_vals()

    def on_L3_y_at_rest(self):
        # print('L Coast')
        # tank_drive(DriveMode.COAST,0,Motors.LEFT)
        # self.cur_drivemode_L = DriveMode.BRAKE
        self.cur_effort_L = 0
        print(self.cur_effort_L)
        self.write_vals()

    def on_R3_up(self,value):
        effort = MAX_SPEED*normalize_joystick(True,value)
        # print(f'R Forward: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.RIGHT)
        # self.cur_drivemode_R = DriveMode.DRIVE
        self.cur_effort_R = effort
        print(self.cur_effort_R)
        self.write_vals()

    def on_R3_down(self,value):
        effort = -1*MAX_SPEED*normalize_joystick(False,value)
        # print(f'R Back: {effort}')
        # tank_drive(DriveMode.DRIVE,effort,Motors.RIGHT)
        # self.cur_drivemode_R = DriveMode.DRIVE
        self.cur_effort_R = effort
        print(self.cur_effort_R)
        self.write_vals()

    def on_R3_y_at_rest(self):
        # print('R Coast')
        # tank_drive(DriveMode.COAST,0,Motors.RIGHT)
        # self.cur_drivemode_R = DriveMode.BRAKE
        self.cur_effort_R = 0
        print(self.cur_effort_R)
        self.write_vals()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()
