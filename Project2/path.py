#!/usr/bin/python3

# ========================================
# ENPM661 Spring 2021: Planning for Autonomous Robots
# Project 2
#
# Author: Siddharth Telang(stelang@umd.edu)
# ========================================

import numpy as np
import matplotlib.pyplot as plt
import math

def isInObstacleSpace(i,j):
    # set a flag 0:false; 1:true
    flag = 0
    #condition for cicle
    circle = (i-90)**2 + (j-70)**2
    if circle <= 1225:
        flag = 1
        print('Tending towards circle ; avoid')
        return flag

    #condition for ellipse
    ellipse = ((i-246)**2)/(60*60) + ((j-145)**2)/(30*30)
    if ellipse <= 1:
        flag = 1
        print('Tending towards ellipse ; avoid')
        return flag

    #condition for rectangle
    line1 = (j - 0.7*i - 74.39)
    line2 = (j - 0.7*i - 98.8)
    line3 = (j + 1.428*i - 176.55)
    line4 = (j + 1.428*i - 439.44)
    print(line1, line2, line3, line4)
    if ((line1 <= 0.0 and line2 >=0.0)  or
            (math.ceil(line1) == 1.0 or math.ceil(line2) == 1.0 or math.ceil(line3) == 1.0 or math.ceil(line4) == 1.0)):
        flag = 1
        print('Tending towards rectangle ; avoid')
        return flag

    return flag