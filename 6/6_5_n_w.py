# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:18:43 2018

@author: nit_n
"""

from numpy import array
from numpy.linalg import solve
from cmath import polar, pi

# define contants
R1 = R3 = R5 = 1000.0
R2 = R4 = R6 = 2000.0
C1 = 1e-6
C2 = 0.5e-6
xplus = 3.0
omega = 1000.0

# set up arrays for the equation solver
# each row is an equation and each column is a term for each equation
# a 0 signifies that there is no term for that
A = array([[1/R1+1/R4+1j*omega*C1, -1j*omega*C1, 0],
           [-1j*omega*C1, 1/R2+1/R5+1j*omega*C1+1j*omega*C2, -1j*omega*C2],
           [0, -1j*omega*C2, 1/R3+1/R6+1j*omega*C2]], complex)

v = xplus*array([1/R1, 1/R2, 1/R3], float)

# calculate the solution
x = solve(A, v)

# convert to polar coordinates and print
r, phi = polar(x[0])
print("V1 amplitude = ", r, "phase = ", phi*180/pi)
r, phi = polar(x[1])
print("V2 amplitude = ", r, "phase = ", phi*180/pi)
r, phi = polar(x[2])
print("V3 amplitude = ", r, "phase = ", phi*180/pi)