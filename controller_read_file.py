import time
import math
from enum import IntEnum
from TankDrive import DriveMode, Motors, tank_drive

# class DriveMode(IntEnum):
#     DRIVE = 1
#     BRAKE = 2
#     COAST = 3
#
# class Motors(IntEnum):
#     LEFT = 1
#     RIGHT = 2

drive_vals = [0,0,DriveMode.COAST,DriveMode.COAST]

def read_vals():
    f = open('actions.txt', 'r')
    lines = f.read().split('\n')
    lines = lines[0:min(4,len(lines))]
    for i, line in enumerate(lines):
        try:
            if i == 2 or i == 3:
                drive_vals[i] = DriveMode(int(line))
            else:
                drive_vals[i] = int(round(float(line)))
        except:
            print('tryingagain')


while True:
    # time.sleep(0.1)
    try:
        read_vals()
        print(drive_vals[2])
        print(drive_vals[0])
        print(Motors.LEFT)

        print(drive_vals[3])
        print(drive_vals[1])
        print(Motors.RIGHT)

        tank_drive(drive_vals[2],drive_vals[0],Motors.LEFT)
        tank_drive(drive_vals[2],drive_vals[0],Motors.RIGHT)

    except KeyboardInterrupt:
        GPIO.cleanup()
        break
