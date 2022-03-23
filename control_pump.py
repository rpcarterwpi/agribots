# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(26, GPIO.OUT)
#


import gpiozero

from time import sleep

led = gpiozero.LED(26)
for i in range(10):
    print('high')
    led.on()
    sleep(0.2)
    led.off()
    print('low')
    sleep(0.2)

# led = PWMLED(2)
#
# for b in range(101):
#     led.value = b / 100.0
#     sleep(0.01)
