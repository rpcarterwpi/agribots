# Agribots MQP Code

## Python on Raspberry Pi

### Older Unused Code

- controller_read_file.py
Used for communication from the controller to an earlier iteration of motor controllers that have since been replaced.

- dead_reckon.py
Code used to initially test the drive system in a straight line, arcs and tank turning.

- localization.py
Math and calculations behind localization used for testing and graphically viewing.

- tank_drive.py
Implements communication and control with older motor controllers.

### Controller Driven

- actions.txt
A file updated each time a command is sent from the PS4 controller.

- control_demo.py
Code originally used for writing PS4 controller actions to a text file to be read by another program.

- demo.py
Code carries out controller actions for the demonstration.

### Main and Sub Systems

- main_rover.py
Imports and unifies the programs explained below to control rover behavior.

- controls.py
Control system code with feedback for PID tank driving.

- encoders.py
Reads and keeps track of encoder direction for each of the four wheels. Estimates forward kinematics for differential drive system.

- gps.py
Calculations for GPS position coordinate systems.

- imu.py
IMU prediction of position using accelerometer and gyroscope.

- mpu9250_i2c.py
Communication with the IMU

- motors.py
Communication with motor controllers and utilizing PID for velocity control.

## Arduino

- Receiver.ino
Contains all logic and behavior for communication and sensing including barometer, temp, wind speed, soil moisture.

- Transmitter.ino
Transmits via RF communication between two arduinos.
