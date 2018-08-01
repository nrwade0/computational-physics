# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:10:35 2018
Newton Method
@author: nit_n
"""

def f(r):
    return -w**2*r**5 + 2*w**2*R*r**4 - w**2*R**2*r**3 + G*(M-m)*r**2 - 2*G*M*R*r + G*M*R**2

# first derivative of f(r)
def df(r):
    return -5*w**2*r**4 + 8*w**2*R*r**3 - 3*w**2*R**2*r**2 + 2*G*(M-m)*r - 2*G*M*R

# constants
G = 6.674e-11 #m3/kg/s2
M = 5.974e25 #kg
m = 7.348e22 #kg
R = 3.844e8 #m
w = 2.662e-6 #/s

accuracy = 1e-11

# initial root guess
x = 3e8

err = 1.0
while err > accuracy:
    delta = f(x)/df(x)
    x -= delta
    err = abs(delta)
        
actual = 3.2639e8 #m
print("actual L1 distance from Earth: ",actual,"m")
print("experimental L1 distance from Earth: ",x,"m")
diff = (actual - x)/actual
print("percent difference: ",abs(diff),"%")