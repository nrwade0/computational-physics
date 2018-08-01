# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:40:57 2018
The Lorenz equations
@author: nit_n
"""

from numpy import arange, array
from pylab import plot, clf, figure, xlabel, ylabel, title

# define some constants
sig = 10
r = 28
b = 8/3

N = 10000
tmin = 0.0
tmax = 50.0
h = (tmax - tmin)/N

# derivatives
def f(s,t):
    x = s[0]
    y = s[1]
    z = s[2]
    
    fx = sig*(y - x)
    fy = r*x - y - x*z
    fz = x*y - b*z
    
    return array([fx, fy, fz], float)

# some initial values
s = array([0, 1, 0], float)
tpoints = arange(tmin, tmax, h)
xpoints = []
ypoints = []
zpoints = []

for t in tpoints:
    xpoints.append(s[0])
    ypoints.append(s[1])
    zpoints.append(s[2])
    
    # now do some runge-kutta (p336)
    k1 = h*f(s, t)
    k2 = h*f(s + 0.5*k1, t + 0.5*h)
    k3 = h*f(s + 0.5*k2, t + 0.5*h)
    k4 = h*f(s + k3, t + h)
    
    s += (k1 + 2*k2 + 2*k3 + k4)/6

figure(1)
clf()
title("part a")
plot(tpoints, ypoints)
xlabel("t")
ylabel("y")

figure(2)
clf()
title("part b")
plot(xpoints, zpoints)
xlabel("x")
ylabel("z")

