# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:22:24 2019

@author: Anique
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

P0 = 101325 #Pa
rho0 = 1.225 #kg/m^3
T0 = 288.15 #K
R = 287.057 # m^2/s^2*K
g0 = 9.80665 #m/s^2
a = -0.0065 #degC/m


def validation(rho0, T0, a):
    alpha = np.genfromtxt("vane_AOA.csv", delimiter=";", dtype="str") #Lijst met AOA in deg
    Vtas = np.genfromtxt("Dadc1_tas.csv", delimiter=";", dtype="str") #Lijst met True Airspeed in knots
    PresAlt = np.genfromtxt("Dadc1_alt.csv", delimiter=";", dtype="str") #Lijst met Pressure Altitude in feet
    