import numpy as np
import math
import matplotlib.pyplot as plt

wheel_base = 1
wheel_track = 1
wheel_radius = 1

def encoder_estimate(enc_vel, pose, pose_cc_dt):
    omega_l, omega_r = min(enc_vel[:,0]), min(enc_vel[:,1])
    v_l, v_r = omega_l * wheel_radius, omega_r * wheel_radius

    print(f'v_l, v_r : {v_l},{v_r}')

    omega = (v_r - v_l)/wheel_track
    print(f'omega: {omega}')


    x, y, theta = pose[0,0], pose[0,1], pose[0,2]
    # print(f'last pose: {x},{y},{theta}')

    if(v_l == v_r):
        R = float('inf')
        ICC = np.array([0,0])
        turn_ee = np.array([ICC[0],ICC[1],R])
        SO3 = np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
        # print(f'rot matrix: \n{SO3}')
        drive_forward = np.array([v_r,0,0])
        # print(f'forward: \n{drive_forward}')

        pose_ee_dot = SO3 @ drive_forward

    else:
        R = (wheel_track/2)*((v_l+v_r)/(v_r-v_l))
        ICC = np.array([x-R*np.sin(theta),y+R*np.cos(theta)])

        # print(f'ICC dist: {R}')
        # print(f'ICC: {ICC}')

        turn_ee = np.array([ICC[0],ICC[1],R])
        d_theta = omega * pose_cc_dt

        SO3_discrete =  np.array([[np.cos(d_theta),-np.sin(d_theta),0],[np.sin(d_theta),np.cos(d_theta),0],[0,0,1]])
        # print(f'rot matrix: \n{SO3_discrete}')
        rel_ICC = np.array([x-ICC[0],y-ICC[1],theta])
        # print(f'rel ICC: {rel_ICC}')
        offset_ICC = np.array([ICC[0],ICC[1],d_theta])
        # print(f'offset ICC: {offset_ICC}')
        pose_ee_dot = SO3_discrete @ rel_ICC + offset_ICC

    pose_ee = pose[0,:] + pose_ee_dot * pose_cc_dt
    pose_ee_ddot = (pose_ee_dot - pose[1,:]) / pose_cc_dt
    pose_ee_full = np.array([pose_ee,pose_ee_dot,pose_ee_ddot])
    # print(f'new pose : \n{np.round(pose_ee_full,2)}')

    return(pose_ee_full,turn_ee)


enc_vel_test = np.array([[0.6,0.5],[0.6,0.5]])
pose_test = np.array([[0,0,math.pi/2],[1,1,0],[0.2,0.2,0.2]])
pose_cc_dt_test = 0.1

x_vals = np.array([pose_test[0,0]])
y_vals = np.array([pose_test[0,1]])

# print(pose_test)
for i in range(10):
    pose_test = encoder_estimate(enc_vel_test,pose_test,pose_cc_dt_test)[0]
    print(pose_test)[0,:]
    x_vals = np.concatenate((x_vals, np.array([pose_test[0,0]])), axis=0)
    y_vals = np.concatenate((y_vals, np.array([pose_test[0,1]])), axis=0)
    # print(pose_test)
# print(x_vals)
# print(y_vals)

#
# xi = pose_test[0,0]
# yi = pose_test[0,1]
# ti = pose_test[0,2]
# xf = new_pose[0,0]
# yf = new_pose[0,1]
# tf = new_pose[0,2]
#
# print(pose_test)
# print(new_pose)

fig, axs = plt.subplots(2, 1)

# xpoints = np.array([xi, xf])
# ypoints = np.array([yi, yf])
axs[0].axis('equal')
# axs[1].axis('equal')
axs[0].plot(x_vals, y_vals)
plt.show()
