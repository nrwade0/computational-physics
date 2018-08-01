# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 15:10:34 2018

@author: nit_n
"""

from gaussxw import gaussxwab
from numpy import linspace, arange
from pylab import plot, show, xlabel, ylabel
from math import pi, exp, sqrt

k = 1.38065e-23 # joules/kelvin
h = 6.626e-34 # joules
lam1 = 390e-9 # meters
lam2 = 750e-9 # meters
c = 3e8 # meters/second

T = linspace(300, 10000, 7000)

part = str(input("what part would you like to do? (a, b, or c) "))

def n(T):
    
    k = 1.38065e-23 # joules/kelvin
    c = 3e8 # meters/second
    
    N = 100
    a = h*c/(lam2*k*T)
    b = h*c/(lam1*k*T)
    x,w = gaussxwab(N,a,b)
    s = 0.0
        
    for k in range(N):
        s += w[k]*(x[k]**3/(exp(x[k])-1))
    
    s = s*(15/(pi*pi*pi*pi))
    return s

if part in ['a'] or ['b']:
    lol = linspace(0, 7000, 7000)
    for i in range(len(T)):
        print("i =",i)
        lol = n(T[i])
        plot(T[i], lol, 'k-')
    show()

if part in ['b']:
    z = (1 + sqrt(5))/2
    accuracy = 1e-6
    x1 = 1/10
    x4 = 1*10
    x2 = x4 - (x4 - x1)/z
    x3 = x1 + (x4 - x1)/z
    
    f1 = n(x1)
    f2 = n(x2)
    f3 = n(x3)
    f4 = n(x4)
    
    while x4-x1>accuracy:
        if f2<f3:
            x4,f4 = x3,f3
            x3,f3 = x2,f2
            x2 = x4 - (x4-x1)/z
            f2 = n(x2)
        else:
            x1,f1 = x2,f2
            x2,f2 = x3,f3
            x3 = x1 - (x4-x1)/z
            f3 = n(x3)

    print("minimum falls at", 0.5*(x1+x4),"K")        
        
        
        