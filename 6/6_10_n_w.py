# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:38:17 2018
pg 259
@author: nit_n
"""

from pylab import plot, show, xlabel, ylabel, clf
from numpy import exp, arange


c = 2
accuracy = 1e-6


def f(x,c):
    return 1- exp(-c*x)

def df(x,c):
    return c*exp(-c*x)


x = 1
epsilon = 1 # eqn 6.83 p256

cpoints = arange(0, 3, 0.01)
xpoints = []

for c in cpoints:
    
    x = 1
    epsilon = 1 # eqn 6.83 p256
    
    while epsilon > accuracy:
        
        xp = f(x,c)
        epsilon = abs((xp-x)/(1-1/df(xp,c)))
        x = xp
        
    xpoints.append(x)
    
clf
plot(cpoints, xpoints)
xlabel("c")
ylabel("solution of x = 1-exp(-cx)")
show()

