import time
import math
import RPi.GPIO as GPIO

RL, FL, RR, FR = 37, 35, 31, 29
IN1, IN2, IN3, IN4 = 22, 24, 26, 36

pwm_freq = 100

GPIO.setmode(GPIO.BOARD)

GPIO.setup(RL, GPIO.OUT)
GPIO.setup(FL, GPIO.OUT)
GPIO.setup(RR, GPIO.OUT)
GPIO.setup(FR, GPIO.OUT)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
print(IN4)
GPIO.setup(IN4, GPIO.OUT)

# setting direction forward
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW)

# setting pwm 100
PWM_FL = GPIO.PWM(FL,pwm_freq)
PWM_FR = GPIO.PWM(FR,pwm_freq)
PWM_RL = GPIO.PWM(RL,pwm_freq)
PWM_RR = GPIO.PWM(RR,pwm_freq)

effort = 100

PWM_FL.start(effort)
PWM_FR.start(effort)
PWM_RL.start(effort)
PWM_RR.start(effort)

time_end = time.time() + 5
a = 0
while time.time() < time_end:
    try:
        a += 1 #does nothing
    except KeyboardInterrupt:
        print('interrupted, cleaning up')
        GPIO.cleanup()
        break
GPIO.cleanup()
