import numpy as np
import matplotlib.pyplot as plt
time = np.genfromtxt("matlab/time.csv", dtype="float")
pitch_rate = np.genfromtxt("matlab/Ahrs1_bPitchRate.csv", dtype="float")
delta_e = np.genfromtxt("matlab/delta_e.csv", dtype="float")
alpha_body = 

#pheugoid 250 sec
for i in range(len(time)):
    if time[i] == 3220.:
        begin_p = i
    if time[i] == 3457.:
        end_p = i


time_p = time[begin_p:end_p]
pitch_rate_p = pitch_rate[begin_p:end_p]
delta_e_p = delta_e[begin_p:end_p]


#short period 15 sec
for i in range(len(time)):
    if time[i] == 3630.:
        begin_s = i
    if time[i] == 3650.:
        end_s = i

time_s = time[begin_s:end_s]
pitch_rate_s = pitch_rate[begin_s:end_s]
delta_e_s = delta_e[begin_s:end_s]

plt.subplot(121)
plt.plot(time_p,pitch_rate_p, label = 'pitch rate')
plt.plot(time_p,delta_e_p, label = 'delta e')
plt.legend()

plt.subplot(122)
plt.plot(time_s,pitch_rate_s, label = 'pitch rate')
plt.plot(time_s,delta_e_s, label = 'delta e')
plt.legend()
plt.show()