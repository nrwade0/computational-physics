# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:52:39 2018

@author: nit_n
"""

from numpy import sin, sqrt, absolute

a = 0
b = 1
eps = 1e-6

def f(x):
    return sin(sqrt(100*x))**2

def trap(a, b, n):
    h = (b - a)/n
    s = (f(a) + f(b))/2
    
    for i in range(1, n):
        s += f(a + i*h)
        
    return(h*s)

def trap_odd(a, b, n):
    
    h = (b - a)/n
    s = 0
    
    for i in range(1, n, 2):
        s += f(a + i*h)
        
    return(h*s)

error = 1
n = 1
i = 0
I = trap(a, b, n)

while error > eps:
    
    if i == 0:
        print("n integral error")
        
    i += 1
    n *= 2
    
    I_1 = I
    I_2 = I_1/2 + trap_odd(a, b, n)
    I = I_2
    
    diff = absolute(I_2 - I_1)/3
    
    print("{:< 7d}".format(n), "{:< 5f}".format(I),"{0:.9f}".format(diff))
    
    error = diff
















