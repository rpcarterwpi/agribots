import numpy as np
import math
import time

import encoders as enc
import motors as mot


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
    pass

def motors_write_raw(motors_write):
    # IN_write, PWM_write = motors_write
    # for i, in_pin in enumerate(IN_pins)
    #     GPIO.output(in_pin, GPIO.HIGH if IN_write[0] == 1 else GPIO.LOW)
    # for i, pwm_pin in enumerate(PWM_pins):
    #     PWM_cur = GPIO.PWM(pwm_pin,pwm_freq)
    #     PWM_cur.start(PWM_write[i])
    pass

# repeated actions
def encoder_actions():
    global enc_vel, enc_pos_data, enc_history, pose, pose_ee, turn_ee, pose_ee_t
    enc_vel, enc_pos_data, enc_history = enc.encoder_measure(encoder_read_raw(),enc_pos_data,enc_history)
    pose_ee, turn_ee, pose_ee_t = enc.encoder_estimate(enc_vel, pose, pose_ee_t)

def controls_actions():
    pass



if __name__ == "__main__":
    pose = np.zeros((3,3))
    enc_vel, enc_pos_data, enc_history, pose_ee, turn_ee, pose_ee_t = enc.encoder_init(pose)

    # ang_vel_cur, ang_vel_desired, motor_error, pid_t, motor_efforts = mot.motor_init()

    while True:
        try:
            encoder_actions()
            print(enc_vel)
            print(pose_ee[0,:])
        except KeyboardInterrupt:
            print(': interupted, cleaning up')
            break
