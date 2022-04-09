# MPU6050 9-DoF Example Printout
from mpu9250_i2c import *

time.sleep(1) # delay necessary to allow mpu9250 to settle

# def imu_estimate(imu_acc, pose, pose_ie_dt, error_axes):
#     x_acc,y_acc,z_acc = imu_acc[0,0],imu_acc[0,2],imu_acc[0,1]
#     pitch_acc,roll_acc,theta_acc = imu_acc[1,0], imu_acc[1,2], imu_acc[1,1]
#
#     pose_ie_ddot = np.array([x_acc,y_acc,pitch_acc])
#     pose_ie_dot = pose[1,:] + (pose_ie_ddot * pose_ie_dt)
#     pose_ie = pose[0,:] + (pose_ie_dot * pose_ie_dt)
#
#     pose_ie_full = np.array([pose_ie,pose_ie_dot,pose_ie_ddot])
#
#     error_axes_ie_ddot = np.array([z_acc,pitch_acc,roll_acc])
#     error_axes_ie_dot = error_axes[1,:] + (error_axes_ie_ddot * pose_ie_dt)
#     error_axes_ie = error_axes[0,:] + (error_axes_ie_dot * pose_ie_dt)
#
#     error_axes_full = np.array([error_axes_ie,error_axes_ie_dot,error_axes_ie_ddot])
#     return(poe_ie_full,error_axes_ie)

print('recording data')
while 1:
    try:
        ax,ay,az,wx,wy,wz = mpu6050_conv() # read and convert mpu6050 data
        mx,my,mz = AK8963_conv() # read and convert AK8963 magnetometer data
    except:
        continue

    print('{}'.format('-'*30))
    print('accel [g]: x = {0:2.2f}, y = {1:2.2f}, z {2:2.2f}= '.format(ax,ay,az))
    print('gyro [dps]:  x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(wx,wy,wz))
    print('mag [uT]:   x = {0:2.2f}, y = {1:2.2f}, z = {2:2.2f}'.format(mx,my,mz))
    print('{}'.format('-'*30))
    time.sleep(1)
