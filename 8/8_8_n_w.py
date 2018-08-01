# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:03:43 2018

@author: nit_n
"""
from numpy import array, sqrt, arange
from pylab import plot, clf, figure, xlabel, ylabel, title

G = 1
M = 10
L = 2
tmin = 0
tmax = 10.0
N = 500
h = (tmax - tmin)/N

def f(r):
    x = r[0]
    y = r[1]
    
    e = sqrt(x**2 + y**2)
    
    vx = r[2]
    vy = r[3]
    
    fx = vx
    fy = vy
    
    fvx = -G*M*x/(e**2 * sqrt(e**2 + L**2/4))
    fvy = -G*M*y/(e**2 * sqrt(e**2 + L**2/4))
    
    return array([fx, fy, fvx, fvy], float)

r = array([1, 0, 0, 1])
xpoints = []
ypoints = []
tpoints = arange(tmin, tmax, h)

for t in tpoints:
    
    # now do some runge-kutta (p336)
    k1 = h*f(r)
    k2 = h*f(r + 0.5*k1)
    k3 = h*f(r + 0.5*k2)
    k4 = h*f(r + k3)
    
    r = r + (k1 + 2*k2 + 2*k3 + k4)/6
    
    xpoints.append(r[0])
    ypoints.append(r[1])
    
figure(1)
clf()
title("Orbit")
plot(xpoints, ypoints)
xlabel("x")
ylabel("y")
