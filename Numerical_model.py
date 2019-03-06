from Cit_par import*
from control import*
from numpy import *

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

sim_sys = ss(A_s, B_s, C_s, D_s)
asim_sys = ss(A_a, B_a, C_a, D_a)