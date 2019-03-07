from Cit_par import*
from control import*
from numpy import *
import matplotlib.pyplot as plt


t_start = 0.
t_end = 100.
dt = 0.1

t = arange(t_start, t_end + dt,dt)


C1_s = np.array([[-2*muc*(c/(Vt0**2)), 0, 0, 0],
                 [0, (CZadot -2*muc)*(c/Vt0), 0, 0],
                 [0, 0, -(c/Vt0), 0],
                 [0, Cmadot*(c/Vt0), 0, -2*muc*KY2*(c/Vt0)**2]])
C2_s = np.array([[CXu*(1/Vt0), CXa, CZ0, CXq*(c/Vt0)],
                 [CZu*(1/Vt0), CZa, -CX0, (CZq+2*muc)*(c/Vt0)],
                 [0,0,0,(c/Vt0)],
                 [Cmu*(1/Vt0), Cma, 0, Cmq*(c/Vt0)]])
C3_s = np.array([[CXde],
                 [CZde],
                 [0],
                 [Cmde]])


C1_a = np.array([[(CYbdot - 2* mub) *(b/Vt0),0,0,0],
                 [0,-0.5*(b/Vt0),0,0],
                 [0,0,-2*mub*KX2*(b/Vt0)**2, 2*mub*KXZ*(b/Vt0)**2],
                 [Cnbdot*(b/Vt0), 0 , 2*mub*KXZ*(b/Vt0)**2 , -2*mub*KZ2*(b/Vt0)**2]])
C2_a = np.array([[CYb,CL,CYp*(b/(2*Vt0)), (CYr -4*mub)*(b/(2*Vt0))],
                 [0,0,(b/(2*Vt0)),0],
                 [Clb,0,Clp*(b/(2*Vt0)), Clr*(b/(2*Vt0))],
                 [Cnb,0,Cnp*(b/(2*Vt0)), Cnr*(b/(2*Vt0))]])
C3_a = np.array([[CYda,CYdr],
                 [0,0],
                 [Clda,Cldr],
                 [Cnda,Cndr]])

A_s = np.matmul(-np.linalg.inv(C1_s),C2_s)
B_s = np.matmul(-np.linalg.inv(C1_s),C3_s)
C_s = np.array([[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]])
D_s = np.array([[0],
       [0],
       [0],
       [0]])

A_a = np.matmul(-np.linalg.inv(C1_a),C2_a)
B_a = np.matmul(-np.linalg.inv(C1_a),C3_a)
C_a = np.array([[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]])
D_a = np.array([[0,0],
       [0,0],
       [0,0],
       [0,0]])

sys_s = ss(A_s, B_s, C_s, D_s)
sys_a = ss(A_a, B_a, C_a, D_a)

#t_s, y_s = impulse_response(sys_s,t, X0 = 0.) 
#t_a, y_a = impulse_response(sys_a,t, X0 = 0.) 

t_s, y_s = step_response(sys_s,t, X0 = 0.) 
t_a, y_a = step_response(sys_a,t, X0 = 0.) 

plt.subplot(121)
plt.plot(t_s, y_s[0])
plt.plot(t_s, y_s[1])
plt.plot(t_s, y_s[2])
plt.plot(t_s, y_s[3])

plt.subplot(122)
plt.plot(t_a, y_a[0])
plt.plot(t_a, y_a[1])
plt.plot(t_a, y_a[2])
plt.plot(t_a, y_a[3])
plt.show()
