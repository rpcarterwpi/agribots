import numpy as np
import math
import time

pid_consts = np.array([0,0,0])
efforts = np.zeros(4)
last_update = time.time()
errors = np.zeros((3,4))
# error = np

def pid(vel_cur, vel_set):
    global pid_consts, efforts, last_update

    cur_update = time.time()
    dt = cur_update - last_update
    last_update = cur_update

    cur_error = vel_set - vel_cur
    errors[1,:] = cur_error * dt
    
