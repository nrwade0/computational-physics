# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:28:43 2018

@author: nit_n
"""

import numpy as np
import pylab as py

# from 0 to 3 in steps of 0.1
a = 0
b = 3
t = 0.1

# number of slices
n = 1000

print("Part A uses Simpson rule")
def f(t):
    return np.exp(t**2)

h = (b - a)/n
s = f(a) + f(b) + 4*f(a + h)

for k in range(1, n//2):
    s += 4*f(a + (2*k + 1)*h) + 2*f(a + 2*k*h)
    
integral = h*s/3

print("output =", integral)

print("")
print("Part B, graph:")

x = list()
y = list()
for i in np.arange(0,3,0.1):
    x.append(i)
    y.append(np.exp(i**2))
    
py.plot(x,y,'-o')
py.show()