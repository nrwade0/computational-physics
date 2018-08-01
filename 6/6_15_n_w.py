# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:36:01 2018
Legendre polynomials: https://en.wikipedia.org/wiki/Legendre_polynomials
@author: nit_n
"""

from numpy import linspace, array, absolute
from pylab import clf, plot, show


def f(x):
    return 924*x**6 - 2772*x**5 + 3150*x**4 - 1680*x**3 + 420*x**2 - 42*x + 1

# first derivative of f(x)
def df(x):
    return 5544*x**5 - 13860*x**4 + 12600*x**3 - 5040*x**2 + 840*x - 42

# plot to find general roots
xplot = linspace(0, 1, 100)
clf()
plot(xplot, f(xplot))
plot([0,1],[0,0])
show()

accuracy = 1e-11

# initial root guess (first three)
x = array([0.03, 0.17, 0.38, 0.63, 0.82, 0.96], float)

for i in range(len(x)):
    err = 1.0
    while err > accuracy:
        delta = f(x[i])/df(x[i])
        x[i] -= delta
        err = absolute(delta)
        
    print(x[i])
    plot(x[i],0,'ko')