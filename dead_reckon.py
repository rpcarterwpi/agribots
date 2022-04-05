import time
import math
from TankDrive import DriveMode, Motors, tank_drive

end_time = time.time() + 30
while time.time() < end_time:
    try:
        tank_drive(DriveMode.DRIVE,-100,Motors.RIGHT)
        tank_drive(DriveMode.DRIVE,100,Motors.LEFT)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
end_time = time.time() + 30
while time.time() < end_time:
    try:
        tank_drive(DriveMode.DRIVE,100,Motors.RIGHT)
        tank_drive(DriveMode.DRIVE,-100,Motors.LEFT)
    except KeyboardInterrupt:
        GPIO.cleanup()
        break



GPIO.cleanup()
