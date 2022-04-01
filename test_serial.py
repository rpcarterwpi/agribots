#!/usr/bin/python
import os, sys
import serial
import time

ser = serial.Serial('/dev/ttyACM0',19200, timeout = 5)

# listen for the input, exit if nothing received in timeout period
while True:
    print(ser.readline())
