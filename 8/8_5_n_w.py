# -*- coding: utf-8 -*-
"""
Created on Mon May  7 17:20:16 2018

@author: nit_n
"""

from numpy import arange, array, sin, cos
from pylab import plot, clf, figure, xlabel, ylabel, show

# define some constants
# resonance frequency will make it look like a standing wave approx 9.7
g = 9.81
l = 0.1
c = 2.0
w = 9.7
a = 0
b = 100
N = 10000

h = (b - a)/N

def f(r, t):
    theta = r[0]
    omega = r[1]
    
    ftheta = omega
    fomega = -g*sin(theta)/l + c*cos(theta)*sin(w*t)
    
    return array([ftheta, fomega], float)

r = array([0, 0], float)
tpoints = arange(a, b, h)
theta_points = []

for t in tpoints:
    
    # now do some runge-kutta (p336)
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6
    
    theta_points.append(r[0])
    
figure(1)
clf()
plot(tpoints, theta_points)
xlabel("t")
ylabel("theta")
show()

print("resonant w value = ", w, " where figure 1 is a standing wave")










