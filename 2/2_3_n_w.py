# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:17:35 2018
2.6
@author: nit_n
"""

# import square root function
from math import atan, sqrt, pi

# ask for inputs
x=float(input("Enter the x coordinate: "))
y=float(input("Enter the y coordinate: "))

# cartesian to polar
r=sqrt(x**2+y**2)
theta=atan(y/x)

# theta to degrees
d=float(theta*(180/pi))

# output
print("r =",r)
print("theta =",d,"(degrees)")