# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:36:17 2018
reference: see all capstone matlab code
@author: nit_n
"""

from numpy import zeros, exp, array
from numpy.linalg import solve
from math import sqrt


# define some constants (all given in part b)
R1 = 1e3
R2 = 4e3
R3 = 3e3
R4 = 2e3

Vp = 5.0
Vt = 5e-2
Io = 3e-9

accuracy = 1e-9

v1 = 1.0
v2 = 1.0

err = 1

J = zeros([2,2])

while err > accuracy:
    # functions 1 and 2 - HW derive f2
    f1 = (v1 - Vp)/R1 + v1/R2 + Io*(exp((v1 - v2)/Vt) - 1)
    f2 = (v2 - Vp)/R3 + v2/R4 - Io*(exp((v1 - v2)/Vt) - 1)
    
    # partial derivatives of function 1
    df1_v1 = 1/R1 + 1/R2 + Io*exp((v1 - v2)/Vt)/Vt
    df1_v2 = -Io*exp((v1 - v2)/Vt)/Vt
    
    # partial derivatives of function 2
    df2_v1 = -Io*exp((v1 - v2)/Vt)/Vt
    df2_v2 = 1/R3 + 1/R4 + Io*exp((v1 - v2)/Vt)/Vt
    
    # fill in Jacobian with partial derivatives
    J[0,0] = df1_v1
    J[0,1] = df1_v2
    J[1,0] = df2_v1
    J[1,1] = df2_v2
    
    # fills second matrix f
    f = array([f1,f2], float)
    
    # solves for the delta x matrix
    dx = solve(J,f)
    
    # places values from delta x matrix into v1 and v2
    v1 -= dx[0]
    v2 -= dx[1]
    
    err = sqrt(dx[0]**2 + dx[1]**2)
    
print("V1 is", v1, "V")
print("V2 is", v2, "V")
print("The difference is", v1 - v2, "V")


