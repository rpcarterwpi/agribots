import time
import math
import RPi.GPIO as GPIO
from TankDrive import DriveMode, Motors, tank_drive

end_time = time.time() + 5
while time.time() < end_time:
    try:
        tank_drive(DriveMode.DRIVE,-100,Motors.RIGHT)
        tank_drive(DriveMode.DRIVE,100,Motors.LEFT)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
end_time = time.time() + 5
while time.time() < end_time:
    try:
        tank_drive(DriveMode.DRIVE,100,Motors.RIGHT)
        tank_drive(DriveMode.DRIVE,-100,Motors.LEFT)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break

GPIO.cleanup()
