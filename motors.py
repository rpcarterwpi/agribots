import numpy as np
import math
import time
from enum import IntEnum

class DriveMode(IntEnum):
    DRIVE = 1
    BRAKE = 2
    COAST = 3

pid_consts = np.array([1,1,1])
int_overflow_lim = 10

IN_forward = np.array([1,0])
IN_back = np.array([0,1])
IN_coast = np.array([1,1])
IN_brake = np.array([0,0])

motors_min_effort = 0
motors_max_effort = 100

# pid_e_consts = np.array([1,1,1])
# int_overflow_lim = 10
# enc_vel_error = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
# enc_vel_cur = np.array([1,2,3,4])
# enc_vel_desired = np.array([2,2,2,2])
# pid_e_t = time.time()


def motor_init():
    motors_active = True
    ang_vel_cur = np.zeros(4)
    ang_vel_desired = np.zeros(4)
    motor_error = np.zeros(3,4)
    pid_t = time.time()
    motor_efforts = np.zeros(4)
    return (motors_active, ang_vel_cur, ang_vel_desired, motor_error, pid_t, motor_efforts)

def motor_pid(ang_vel_cur, ang_vel_desired, motor_error, pid_t):
    pid_t_cur = time.time()
    pid_dt = pid_t_cur - pid_t

    error = ang_vel_cur - ang_vel_desired
    error_int = np.clip(motor_error[1,:] + (error * pid_dt), -int_windup, int_windup)
    error_dot = (error - motor_error[0,:] / pid_dt)

    error_full = np.array([error, error_int, error_dot])
    efforts = error_full.T @ pid_consts
    return (efforts, error_full, pid_t)

def control_drive(efforts,drive_mode = DriveMode.DRIVE):
    out = zeros()
    if drive_mode == DriveMode.DRIVE:
        IN_write[0:2] = IN_forward if efforts[0] >= 0 else IN_back
        IN_write[2:4] = IN_forward if efforts[1] >= 0 else IN_back
        PWM_write = np.clip(np.rint(efforts),motors_min_effort,motors_max_effort)
    else:
        if(drive_mode == DriveMode.COAST):
            IN_write = IN_coast
        else:
            IN_write = IN_brake
        PWM_write = np.zeros(4)
    return (IN_write, PWM_write)
