# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:31:51 2019

@author: Sybren
"""
from math import *

def velocity(V_IAS,hp,Tm):
    p0 = 101325             #Pa ISA
    rho0 = 1.225            #Kg/m3
    lapse = -6.5 * 10**(-3)     #deg C/m
    T0 = 288.15
    R = 287.057
    g0= 9.80665
    gamma = 1.4
    
    Vc = (V_IAS - 2)*0.514444
    p = p0 * (1 + (lapse * hp)/T0)**(-g0/(lapse*R))
    M = sqrt(2/(gamma - 1)* ( (1+(p0/p)*((1+(gamma-1)/(2*gamma) * (rho0/p0)*Vc*Vc)**(gamma/(gamma-1)) - 1))**((gamma - 1)/gamma) - 1))
    T = Tm / (1 + (gamma-1)/2 * M**2.)
    a = sqrt(gamma*R*T)
    Vt = M*a
    rho = rho0 * (T/T0)**(-(g0/(lapse*R) + 1))
    Ve = Vt * sqrt(rho/rho0)
    
    return Vc, M, a, Vt, Ve, rho
    

V_IAS = 249        #m/s
hp = 5010*0.3048
Tm = 12.5 + 273.15

v = velocity(V_IAS, hp, Tm)
    
    
    