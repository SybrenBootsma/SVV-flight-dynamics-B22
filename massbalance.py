# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:55:08 2019

@author: Hidde Jansen
"""
import numpy as np
import matplotlib.pyplot as plt

lbskg = 0.453592

Fmom = [298.16, 591.18, 879.08, 1165.42, 1448.40, 1732.53, 2014.80, 2298.84, 2581.92, 2866.30, 3150.18, 3434.52, 3718.52, 4003.23, 4287.76, 4572.24, 4856.56, 5141.16, 5425.64, 5709.90, 5994.04, 6278.47, 6562.82, 6846.96, 7131.00, 
7415.33, 7699.60, 7984.34, 8269.06, 8554.05, 8839.04, 9124.80, 9410.62, 9696.97, 9983.40, 10270.08, 10556.84, 10843.87, 11131.00, 11418.20, 11705.50, 11993.31, 12281.18, 12569.04, 12856.86, 13144.73, 13432.48, 13720.56, 14008.46, 14320.34]
Fmlist = list(np.arange(100., 5000., 100.)) + [5008.]
Ftot = 4050.

MP1 = 95./lbskg
MP2 = 92./lbskg
MCL = 0./lbskg
MCR = 74./lbskg
M1L = 66./lbskg
M1R = 61./lbskg
M2L = 75./lbskg
M2R = 78./lbskg
M3L = 86./lbskg  
M3R = 68./lbskg
xP = 131.
xC = 170.
x1 = 214.
x2 = 251.
x3 = 288.
BEM = 9165. 
xB = 292.18
g0 = 9.80665
inmet = 0.0254


time = np.genfromtxt("matlab/time.csv", dtype="float")
FUR = np.genfromtxt("matlab/rh_engine_FU.csv", dtype="float")
FUL = np.genfromtxt("matlab/lh_engine_FU.csv", dtype="float")



def massbalance(t):
    xcg = []
    W = []
    for i in range(len(t)):
        Fm = Ftot - (FUR[i] + FUL[i])
        Mom = BEM*xB + (MP1+MP2)*xP + (MCL+MCR)*xC + (M1L+M1R)*x1 + (M2L+M2R)*x2 + (M3L+M3R)*x3 + (np.interp(Fm, Fmlist, Fmom))*100.
        # Weight in N
        Wi = BEM + MP1 + MP2 + MCL + MCR + M1L + M1R + M2L + M2R + M3L + M3R + Fm 
        # xcg in m w.r.t. LEMAC
        xcg.append(((Mom/Wi)-261.45)*inmet)
        W.append(Wi*lbskg*g0)
    return (xcg, W)

#plt.plot(time, massbalance(time)[1])
#plt.show()
print(massbalance([9.2]))