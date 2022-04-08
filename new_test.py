import time
import math
import RPi.GPIO as GPIO

motor_RL, motor_FL, motor_RR, motor_FR = 37, 35, 31, 29
IN1, IN2, IN3, IN4 = 22, 24, 26, 36

enc_RL, enc_FL, enc_RR, enc_FR = 16, 18, 11, 13

PWM_freq = 100

GPIO.setmode(GPIO.BOARD)

GPIO.setup(motor_RL, GPIO.OUT)
GPIO.setup(motor_FL, GPIO.OUT)
GPIO.setup(motor_RR, GPIO.OUT)
GPIO.setup(motor_FR, GPIO.OUT)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.setup(enc_RL, GPIO.IN)
GPIO.setup(enc_FL, GPIO.IN)
GPIO.setup(enc_RR, GPIO.IN)
GPIO.setup(enc_FR, GPIO.IN)

# setting direction forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)

# setting pwm 100
PWM_FL = GPIO.PWM(motor_FL,PWM_freq)
PWM_FR = GPIO.PWM(motor_FR,PWM_freq)
PWM_RL = GPIO.PWM(motor_RL,PWM_freq)
PWM_RR = GPIO.PWM(motor_RR,PWM_freq)

effort = 80

PWM_FL.start(effort)
PWM_FR.start(effort)
PWM_RL.start(effort)
PWM_RR.start(effort)


def encoder_measure(enc_pos,):
    enc_pos_cur = np.array([GPIO.input(enc_FL),GPIO.input(enc_FR),GPIO.input(enc_RL),GPIO.input(enc_RR)])



time_end = time.time() + 5
a = 0
while time.time() < time_end:
    try:
        print(GPIO.input(enc_RL))
    except KeyboardInterupt:
        print('interupted, cleaning up')
        GPIO.cleanup()
        break
GPIO.cleanup()
