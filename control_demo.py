import time
import math
from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L3_left(self, value):
        a = 0

    def on_L3_right(self, value):
        a = 0

    def on_R3_left(self, value):
        a = 0

    def on_R3_right(self, value):
        a = 0


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
