from Cit_par import*
from control import*
import numpy as np

C1_s = np.array([[-2*muc*(c/(Vto**2)), 0, 0, 0],
                 [0, (CZadot -2*muc)*(c/Vto), 0, 0],
                 [0, 0, -(c/Vto), 0],
                 [0, Cmadot*(c/Vto), 0, -2*muc*KY2*(c/Vto)**2]])
C2_s = np.array([[CXu*(1/Vto), CXa, CZ0, CXq*(c/Vto)],
                 [CZu*(1/Vto), CZa, -CX0, (CZq+2*muc)*(c/Vto)],
                 [0,0,0,(c/Vto)],
                 [Cmu*(1/Vto), Cma, 0, Cmq*(c/Vto)]])
C3_s = np.array([[CXde],
                 [ZCde],
                 [0],
                 [CMde]])


C1_a = np.array([[(CYbdot - 2* mub) *(b/Vt0),0,0,0],
                 [0,-0.5*(b/Vt0),0,0],
                 [0,0,-2*mub*KX2*(b^2/Vt0^2), 2*mub*KXZ*(b^2/Vt0^2)],
                 [Cnbdot*(b/Vt0), 0 , 2*mub*KXZ*(b^2/Vt0^2) , -2*mub*KZ2*(b^2/Vt0^2)]])

C2_a = np.array([[CYb,CL,CYp*(b/(2*Vt0)), (CYr -4*mub)*(b/(2*Vt0))],
                 [0,0,(b/(2*Vt0)),0],
                 [Clb,0,Clp*(b/(2*Vt0)), Clr*(b/(2*Vt0))],
                 [Cnb,0,Cnp*(b/(2*Vt0)), Cnr*(b/(2*Vt0))]])

C3_a = np.array([[CYa,CYdr],
                 [0,0],
                 [Clda,Cldr],
                 [Cnda,Cndr]])


A_s = []
B_s = []
C_s = np.array([[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]])

D_s = np.array([[0],
       [0],
       [0],
       [0]])


A_a = []
B_a = []
C_a = np.array([[1,0,0,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,1]])
D_a = np.array([[0,0],
       [0,0],
       [0,0],
       [0,0]])