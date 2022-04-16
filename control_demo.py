import time
import math
from pyPS4Controller.controller import Controller
import RPi.GPIO as GPIO

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()
