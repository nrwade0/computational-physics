# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:52:39 2018

@author: nit_n
"""

import numpy as np
import pylab as py

data = np.loadtxt('velocities.txt')

# some constants
n = 1000
a = 0
b = int(100)
h = (b - a)/n

def f(t):
    # find our appropriate y values for our x's
    t = int(t)
    return data[t,1]

bum = (f(a)+f(b))/2
glum = 0

for k in range(1, n-1):
    glum += f(a + k*h)
    
integral = (glum + bum)*h
print("integral =", integral)

for i in range(0,100):
    py.plot(data[i,0],data[i,1],'ko')

py.jet()
py.colorbar
py.show()