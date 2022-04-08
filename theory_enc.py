import numpy as np
import math
import time

enc_history_size = 100
enc_rot_per_tick =  np.array([0.1,0.101,0.09,0.08])


enc_pos = np.array([0,0,0,0])
enc_m_i = -1
enc_m_t = time.time()

enc_d_history =  np.zeros((enc_history_size,4))
enc_t_history = np.zeros(enc_history_size)

enc_pos_data = (enc_pos,enc_m_i,enc_m_t)
enc_history = (enc_d_history,enc_t_history)


def encoder_measure(enc_pos_data,enc_history):

    enc_pos, enc_m_i, enc_m_t = enc_pos_data
    enc_d_history, enc_t_history = enc_history

    enc_pos_cur = np.random.randint(0,2,4)
    enc_m_i_cur = (enc_m_i+1) % enc_history_size
    enc_m_t_cur = time.time()

    enc_d_history[enc_m_i_cur,:] = np.abs(enc_pos_cur - enc_pos)
    enc_t_history[enc_m_i_cur] = enc_m_t_cur - enc_m_t

    enc_tick_per_sec = np.sum(enc_d_history,axis = 0) / np.sum(enc_t_history)
    enc_vel = enc_tick_per_sec * enc_rot_per_tick * 2 * math.pi

    return (enc_vel,(enc_pos_cur,enc_m_i_cur,enc_m_t_cur),(enc_d_history,enc_t_history))

def encoder_measure(enc_raw, enc_pos_data, enc_history):



time_end = time.time()+10
while time.time() < time_end:
    time.sleep(0.01)
    enc_vel, enc_pos_data, enc_history = encoder_measure(enc_pos_data,enc_history)
    # print(enc_history[0])
    print(enc_vel)
