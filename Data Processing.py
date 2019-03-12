# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:01:51 2019

@author: Anique
"""
import numpy as np
import matplotlib.pyplot as plt

# Standard values used for calculation
P0 = 101325 #Pa
rho0 = 1.225 #kg/m^3
T0 = 288.15 #K
R = 287.057 # m^2/s^2*K
g0 = 9.80665 #m/s^2
lapse = -0.0065 #degC/m
S = 30.0 #m^2
BEW = 9165.0 #lbs

def data_processing(BEW, Vt, rho, S, T):
    # Data from Stationary Measurement to calculate Cl, CD
    hp1 = np.array([5010, 5020, 5020, 5030, 5020, 5110]) #Pressure Altitude in ft
    IAS1 = np.array([249, 221, 192, 163, 130, 118]) #Indicated Airspeed in knots
    AOA1 = np.array([1.7, 2.4, 3.6, 5.4, 8.7, 10.6]) #Angle of Attack in deg
    FFL1 = np.array([798, 673, 561, 463, 443, 474]) #Fuel Flow Left in lbs/hr
    FFR1 = np.array([813, 682, 579, 484, 467, 499]) #Fuel Flow Right in lbs/hr
    Fused1 = np.array([360, 412, 447, 478, 532, 570]) #Fuel used in lbs
    TAT1 = np.array([12.5, 10.5, 8.8, 7.2, 6, 5.2]) #Total air temperature in Celsius
    
    
    # Data from Stationary Measurement to calculate Cmalpha, Cmdelta
    hp2 = np.array([6060, 6350, 6550, 6880, 6160, 5810, 5310]) #Pressure Altitude in ft
    IAS2 = np.array([161, 150, 140, 130, 173, 179, 192]) #Indicated Airspeed in knots
    AOA2 = np.array([5.3, 6.3, 7.3, 8.5, 4.5, 4.1, 3.4]) #Angle of Attack in deg
    Deltae2 = np.array([0, -0.4, -0.9, -1.5, 0.4, 0.6, 1]) #Elevator Deflection in deg
    Deltaetr2 = np.array([2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8]) #Elevator trim tab Deflection in deg
    StickF2 = np.array([0, -23, -29, -46, 26, 40, 83]) #Stick Force in Newton
    FFL2 = np.array([462, 458, 454, 449, 465, 472, 482]) #Fuel Flow Left in lbs/hr
    FFR2 = np.array([486, 482, 477, 473, 489, 496, 505]) #Fuel Flow Right in lbs/hr
    Fused2 = np.array([664, 694, 730, 755, 798, 825, 846]) #Fuel used in lbs
    TAT2 = np.array([5.5, 4.5, 3.5, 2.5, 5.0, 6.2, 8.2]) #Total air temperature in Celsius
    
    
    # Calculation of Cl and Cd, plot Cl-alpha, Cd-alpha, Cl-Cd graphs
    Mfuel = 4050 #lbs
    Mperson = 695 #kg
    
    Mtotal = BEW*0.453592 + Mfuel*0.453592 + Mperson - Fused1 #Total mass in kg
    W = Mtotal*9.81     #Weight in Newton
    
    Cl = W/(0.5*rho*ISA1^2*S)
    Cd = T/(0.5*rho*IAS1^2*S)
    plt.plot(AOA1, Cl)
    plt.plot(AOA1, Cd)
    plt.plot(Cl, Cd)