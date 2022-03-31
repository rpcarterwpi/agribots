# Imported Libraries
import RPi.GPIO as GPIO
from time import sleep

# SetMode
GPIO.setmode(GPIO.BOARD)

class DriveMode(Enum):
    DRIVE = 1
    BRAKE = 2
    COAST = 3

class Motors(Enum):
    LEFT = 1
    RIGHT = 2
    PUMP = 3

# Left Setup
ENA1, IN1, IN2 = 33, 29, 31
GPIO.setup(ENA1, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

# Right Setup
ENA2, IN3, IN4 = 32, 16, 18
GPIO.setup(ENA2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

PWM_FREQ = 100
MAX_SPEED = 100

tank_drive(mode,effort,motor):
    if motor == Motors.LEFT:
        ENA = ENA1
        INA = IN1
        INB = IN2
    elif motor == Motors.RIGHT:
        ENA = ENA2
        INA = IN3
        INB = IN4

    if mode == DriveMode.DRIVE:
        forward = effort/abs(effort) >= 0
        if forward:
            GPIO.output(INA, GPIO.HIGH)
            GPIO.output(INB, GPIO.LOW)
        else
            GPIO.output(INA, GPIO.LOW)
            GPIO.output(INB, GPIO.HIGH)

    elif mode == DriveMode.BRAKE:
        GPIO.output(INA, GPIO.LOW)
        GPIO.output(INB, GPIO.LOW)

    elif mode == DriveMode.COAST:
        GPIO.output(INA, GPIO.HIGH)
        GPIO.output(INB, GPIO.HIGH)

    PWM_cur = GPIO.PWM(ENA,PWM_FREQ)
    PWM_cur.start(abs(effort))

tank_drive(DriveMode.DRIVE,100,Motors.LEFT)
tank_drive(DriveMode.DRIVE,100,Motors.RIGHT)

sleep(5)
GPIO.cleanup()
