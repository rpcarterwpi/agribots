# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(26, GPIO.OUT)
#


import gpiozero

from time import sleep
# or 37
# led = gpiozero.LED(37)
# led.on()
# sleep(5)
# for i in range(10):
#     print('high')
#     led.on()
#     sleep(1)
#     led.off()
#     print('low')
#     sleep(1)
led1 = gpiozero.LED(37)
led2 = gpiozero.LED(26)
led1.off()
led2.off()
sleep(5)

# led = gpiozero.PWMLED(37)
# led.value = 0.5
# sleep(5)
# led2 = gpiozero.PWMLED(26)
#
# for i in range(10):
    # for b in range(101):
    #     led.value = b / 100.0
    #     # led2.value = b / 100.0
    #     sleep(0.01)
