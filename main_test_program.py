import numpy as np
import math
import time

import encoders as enc
import motors as mot
import imu
import gps
import path_planner as path


# uses dependencies like GPIO that cannot be tested easily
# has the master pinout of raspi

# encoder pins
pin_enc_RL, pin_enc_FL, pin_enc_RR, pin_enc_FR = 16, 18, 11, 13
# pwm pins
pin_motor_RL, pin_motor_FL, pin_motor_RR, pin_motor_FR = 37, 35, 31, 29
PWM_pins = [pin_motor_RL, pin_motor_FL, pin_motor_RR, pin_motor_FR]
# direction pins
pin_IN1, pin_IN2, pin_IN3, pin_IN4 = 22, 24, 26, 36
IN_pins = [pin_IN1, pin_IN2, pin_IN3, pin_IN4]

pwm_freq = 100

def encoder_read_raw():
    # return np.array([GPIO.input(enc_FL),GPIO.input(enc_FR),GPIO.input(enc_RL),GPIO.input(enc_RR)])
    return np.random.randint(0,2,4) #dummy random bits

def gps_read_raw():
    pass

def imu_read_raw():
    # ax,ay,az,wx,wy,wz = MPU6050_conv() # read and convert mpu6050 data
    # mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
    # return np.array([ax, ay, az, wx, wy, wz, mx, my, mz])
    return np.array([0,1,2,3,4,5,6,7,8])

def motors_write_raw(motors_write):
    # IN_write, PWM_write = motors_write
    # for i, in_pin in enumerate(IN_pins)
    #     GPIO.output(in_pin, GPIO.HIGH if IN_write[0] == 1 else GPIO.LOW)
    # for i, pwm_pin in enumerate(PWM_pins):
    #     PWM_cur = GPIO.PWM(pwm_pin,pwm_freq)
    #     PWM_cur.start(PWM_write[i])
    print('writing motors:')
    print(motors_write)
    # pass

# repeated actions
def encoder_actions():
    global enc_vel, enc_pos_data, enc_history, pose, pose_ee, turn_ee, pose_ee_t
    enc_vel, enc_pos_data, enc_history = enc.encoder_measure(encoder_read_raw(),enc_pos_data,enc_history)
    pose_ee, turn_ee, pose_ee_t = enc.encoder_estimate(enc_vel, pose, pose_ee_t)

def imu_actions():
    global imu_data, pose, pose_ie_t, error_axes, pose_ie
    imu_data = imu_read_raw()
    pose_ie, error_axes, pose_ie_t = imu.imu_estimate(imu_data, pose, pose_ie_t, error_axes)

def controls_actions():
    global motors_active, ang_vel_cur, ang_vel_desired, motor_error, pid_t, motor_efforts
    if motor_active:
        mot.motor_pid()
        mot.control_drive()

    pass

def localization_actions():
    # fusion of pos_ee, pose_ie, pose_ge to pose
    pass



if __name__ == "__main__":
    pose = np.zeros((3,3))

    enc_vel, enc_pos_data, enc_history, pose_ee, turn_ee, pose_ee_t = enc.encoder_init(pose)
    imu_data, pose_ie, error_axes, pose_ie_t = imu.imu_init(pose)
    motors_active, ang_vel_cur, ang_vel_desired, motor_error, pid_t, motor_efforts = mot.motor_init()

    while True:
        try:
            encoder_actions()
            imu_actions()
            print(pose_ie[0,:])
            # print(enc_vel)
            # print(pose_ee)
        except KeyboardInterrupt:
            print(': interupted, cleaning up')
            break
