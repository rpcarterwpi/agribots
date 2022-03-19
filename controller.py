from pyPS4Controller.controller import Controller
import time
from dual_max14870_rpi import motors, MAX_SPEED
import math

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    # def on_x_press(self):
    #    print("Hello world")
    def on_L3_up(self,value):
        new_value = max(0.0,min(1.0,abs((value+281)/-32486)))
        print(f'UP! {new_value}')
        motors.motor1.setSpeed(new_value*MAX_SPEED)
        # -281 -> -32767
        # motors.motor1.setSpeed(s)

    def on_L3_left(self,value):
        value = 0

    def on_L3_right(self,value):
        value = 0

    def on_L3_down(self,value):
        new_value = max(0.0,min(1.0,abs((value-281)/32486)))
        print(f'DOWN! {new_value}')
        motors.motor1.setSpeed(new_value*MAX_SPEED*-1)

    def on_L3_y_at_rest(self):
        print('reset motors')
        motors.motor1.setSpeed(0)



controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=True)
controller.listen()
