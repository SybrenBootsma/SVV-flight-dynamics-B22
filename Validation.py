# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:22:24 2019

@author: Anique
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

def validation():
    alpha = np.genfromtxt("flightdata.vane_AOA.csv", delimiter=";", dtype="str", skip_header=1) #Lijst met AOA in deg
    Vtas = np.genfromtxt("flightdata.Dadc1_tas.csv", delimiter=";", dtype="str", skip_header=1) #Lijst met True Airspeed in knots
    
    