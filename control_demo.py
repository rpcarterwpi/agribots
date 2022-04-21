import time
import math
from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO

l_index = 0
r_index = 1
arm_index = 2

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        self.pass_args = [0,0,0]
        self.write_vals()

    def write_vals(self):
        f = open('actions.txt', 'w')
        write_str = ','.join([str(arg) for arg in self.pass_args])
        f.write(write_str)
        f.close()

    def on_L3_up(self, value):
        value = value/-32767
        self.pass_args[l_index] = value
        self.write_vals()
        print(f'left: {value}')

    def on_L3_down(self, value):
        value = value/-32767
        self.pass_args[l_index] = value
        self.write_vals()
        print(f'left: {value}')

    def on_L3_y_at_rest(self):
        value = 0
        self.pass_args[l_index] = value
        self.write_vals()
        print(f'left: {value}')

    def on_R3_up(self, value):
        value = value/-32767
        self.pass_args[r_index] = value
        self.write_vals()
        print(f'right: {value}')

    def on_R3_down(self, value):
        value = value/-32767
        self.pass_args[r_index] = value
        self.write_vals()
        print(f'right: {value}')

    def on_R3_y_at_rest(self):
        value = 0
        self.pass_args[r_index] = value
        self.write_vals()
        print(f'right: {value}')

    def on_L3_left(self, value):
        a = 0

    def on_L3_right(self, value):
        a = 0

    def on_R3_left(self, value):
        a = 0

    def on_R3_right(self, value):
        a = 0

    def on_L3_x_at_rest(self):
        a = 0

    def on_R3_x_at_rest(self):
        a = 0

    def on_x_press(self):
        self.pass_args[arm_index] = 1
        print('arm 1')
        self.write_vals()

    def on_x_release(self):
        self.pass_args[arm_index] = 0
        print('arm 0')
        self.write_vals()




controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
