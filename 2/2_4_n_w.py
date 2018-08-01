# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:17:35 2018
2.4
@author: nit_n
"""

# import square root function
from math import sqrt

# ask for inputs of distance and speed
x=float(input("Enter the distance away in light years: "))
v=float(input("Enter the speed as a fraction of the speed of light (c): "))

# time for observer on Earth in years
ta=x/v

# Lorentz factor
gamma=1/sqrt(1-v**2)

# time dilation for someone on a space ship near c
tb=ta/gamma

# output block
print("part a")
print("t =",ta,"years")
print("part b")
print("t =",tb,"years")