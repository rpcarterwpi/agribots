# general imports
import numpy as np
import math
import time

# for gps
import os, sys
# import serial

# written agribots files
import encoders as enc
from motors import DriveMode
import motors as mot
import imu
import gps
import path_planner as path

from mpu9250_i2c import *

# for raspi
import RPi.GPIO as GPIO


# uses dependencies like GPIO that cannot be tested easily
# has the master pinout of raspi

# encoder pins
pin_enc_RL, pin_enc_FL, pin_enc_RR, pin_enc_FR = 16, 18, 11, 13
enc_pins = [pin_enc_FL, pin_enc_FR, pin_enc_RL, pin_enc_RR]
# pwm pins
pin_motor_RL, pin_motor_FL, pin_motor_RR, pin_motor_FR = 37, 35, 31, 29
PWM_pins = [pin_motor_FL, pin_motor_FR, pin_motor_RL, pin_motor_RR]
# direction pins
pin_IN1, pin_IN2, pin_IN3, pin_IN4 = 22, 24, 26, 36
IN_pins = [pin_IN1, pin_IN2, pin_IN3, pin_IN4]

pwm_freq = 100

def init_pins():
    GPIO.setmode(GPIO.BOARD)
    for pin in IN_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in PWM_pins:
        GPIO.setup(pin, GPIO.OUT)
    for pin in enc_pins:
        GPIO.setup(pin, GPIO.IN)

def encoder_read_raw():
    #! comment in with raspi
    out = np.zeros(4)
    for i, pin in enumerate(enc_pins):
        out[i] = GPIO.input(pin)
    return out
    # return np.array([GPIO.input(pin_enc_FL),GPIO.input(pin_enc_FR),GPIO.input(pin_enc_RL),GPIO.input(pin_enc_RR)])
    # return np.random.randint(0,2,4) #dummy random bits

def gps_read_raw():
    pass

def imu_read_raw():
    # #! comment in with raspi
    # ax,ay,az,wx,wy,wz = MPU6050_conv() # read and convert mpu6050 data
    # mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
    # data = np.array([ax, ay, az, wx, wy, wz, mx, my, mz])
    # # return
    # print(data)
    # # return np.array([0,1,2,3,4,5,6,7,8])
    mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
    # data = np.array([mx,my,mz])
    return np.array([mx,my,mz])

def motors_write_raw(motors_write):
    #! comment in with raspi
    IN_write, PWM_write = motors_write
    for i, in_pin in enumerate(IN_pins):
        GPIO.output(in_pin, GPIO.HIGH if IN_write[i] == 1 else GPIO.LOW)
    for i, pwm_pin in enumerate(PWM_pins):
        PWM_cur = GPIO.PWM(pwm_pin,pwm_freq)
        PWM_cur.start(PWM_write[i])
        time.sleep(1/pwm_freq)
    # print('writing motors:')
    # print(motors_write)
    # pass

# repeated actions
def encoder_actions():
    global enc_vel, enc_pos_data, enc_history, pose, pose_ee, turn_ee, pose_ee_t, motor_dir
    enc_vel, enc_pos_data, enc_history = enc.encoder_measure(encoder_read_raw(),enc_pos_data,enc_history, motor_dir)
    pose_ee, turn_ee, pose_ee_t = enc.encoder_estimate(enc_vel, pose, pose_ee_t)

def imu_actions():
    # global imu_data, pose, pose_ie_t, error_axes, pose_ie
    global cur_heading
    imu_mag_data = imu_read_raw()
    cur_heading = imu.imu_mag(imu_mag_data)

    # pose_ie, error_axes, pose_ie_t = imu.imu_estimate(imu_data, pose, pose_ie_t, error_axes)

def controls_actions():
    global motors_active, drive_mode, enc_vel, ang_vel_desired, motor_error, pid_t, motor_efforts, motor_dir
    if motors_active:
        #! maybe change ang_vel_cur = enc_vel????
        motor_efforts, motor_error, pid_t, motor_dir = mot.motor_pid(enc_vel, ang_vel_desired, motor_error, pid_t, motor_efforts, motor_dir)
        #! omitting drive_mode for now?????
        # motor_efforts = np.array([-100,100,-100,100])
        motors_write = mot.control_drive(motor_efforts)
        motors_write_raw(motors_write)
        #! allow one cycle of pwm??????
        # time.sleep(1/pwm_freq)

def localization_actions():
    global pose_ee, pose, cur_heading
    # fusion of pos_ee, pose_ie, pose_ge to pose
    pose = pose_ee
    pose[0,2] = cur_heading
    # pass

def path_planning_actions():

    pass

def read_vals():
    global ang_vel_desired
    f = open('actions.txt', 'r')
    lines = f.read().split('\n')
    # print(lines)
    # lines = lines[0:min(2,len(lines))]
    try:
        for i, line in enumerate(lines):
            if i == 0:
                ang_vel_desired[0] = float(line)
                ang_vel_desired[2] = float(line)

            elif i == 1:
                ang_vel_desired[1] = float(line)
                ang_vel_desired[3] = float(line)
    except:
        print('cannot_read')


if __name__ == "__main__":

    init_pins()
    pose = np.zeros((3,3))

    enc_vel, enc_pos_data, enc_history, pose_ee, turn_ee, pose_ee_t = enc.encoder_init(pose)

    # imu_data, pose_ie, error_axes, pose_ie_t = imu.imu_init(pose)
    cur_heading = imu.imu_mag_init()

    motors_active, drive_mode, ang_vel_desired, motor_error, pid_t, motor_efforts, motor_dir = mot.motor_init()

    # temporary
    # ang_vel_desired = np.array([-1.6,1.6,-1.6,1.6])


    # calibrate encoders first
    start_time = time.time() + 1
    print('calibrating')
    motors_active = False
    while time.time() < start_time:
        encoder_actions()
    motors_active = True
    print('starting')

    while True:
        try:
            encoder_actions()
            controls_actions()
            localization_actions()
            imu_read_raw()
            imu_actions()

            read_vals()
            # print(ang_vel_desired)
            print(pose[0,:])


            # print(f'mag: {cur_heading}, theta: {pose[0,2]*(180/math.pi)}')
            # print(cur_heading)


            # print('error')
            # print(motor_error[0,:])

            # print('desired')
            # print(ang_vel_desired)
            # print(f'actual: {round(enc_vel[1],2)}, error: {round(motor_error[0,1],2)}, effort: {round(motor_efforts[1],2)}')
            # print(enc_vel)

            # print(pose[0,:])
            # print('error')
            # print(motor_error[0,:])
            # print('efforts')
            # print(motor_efforts[1])

            # print('efforts:')
            # print(motor_efforts)
            # motors_write_raw((IN_write,PWM_write)) #force writing
            # print(enc_vel/(2*math.pi)) # rpm
            # print(motor_error[0,:])
            # print(ang_vel_desire)
            # imu_actions()
            # controls_actions()


        except KeyboardInterrupt:
            print(': interupted, cleaning up')
            break
