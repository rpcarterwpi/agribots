import numpy as np

wheel_base = 1
wheel_track = 1
wheel_radius = 1


enc_vel_test = np.array([[1,2],[3,4]])
pose_test = np.array([[1,2,3],[4,5,6],[7,8,9]])
pose_cc_dt_test = 10

def encoder_estimate(enc_vel, pose, pose_cc_dt):
    omega_l, omega_r = min(enc_vel[:,0]), min(enc_vel[:,1])
    v_l, v_r = omega_l * wheel_radius, omega_r * wheel_radius

    omega = (v_r - v_l)/wheel_track

    if(v_l == v_r):
        R = float('inf')
    else:
        R = (wheel_track/2)*((v_l+v_r)/(v_r-v_l))

    x, y, theta = pose[0,0], pose[0,1], pose[0,2]
    ICC = np.array([x-R*np.sin(theta),y+R*np.cos(theta)])

    d_theta = omega * pose_cc_dt

    SO3_discrete =  np.array([[np.cos(d_theta),-np.sin(d_theta),0],[np.sin(d_theta),-np.cos(d_theta),0],[0,0,1]])
    rel_ICC = np.array([x-ICC[0],y-ICC[1],theta])
    offset_ICC = np.array([ICC[0],ICC[1],d_theta])

    pose_ee_dot = SO3_discrete @ rel_ICC + offset_ICC

    print(pose_ee_dot)
    # 
    #
    # print(v_l)
    # print(v_r)
    # print(pose)
    # print(pose_cc_dt)

encoder_estimate(enc_vel_test,pose_test,pose_cc_dt_test)
