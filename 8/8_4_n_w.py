# -*- coding: utf-8 -*-
"""
Created on Sat May 12 15:16:41 2018
numpy.sine function must be in radians, documentation: https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.sin.html
@author: nit_n
"""

from numpy import sin, array, arange, pi, cos
from pylab import plot, clf, figure, xlabel, ylabel, title
from vpython import sphere, canvas, vector, color, rate

g = 9.81
l = 0.1
tmin = 0.0
tmax = 20.0
N = 1000
h = (tmax - tmin)/N

# theta must be in radians for numpy.sin
def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/1)*sin(theta)
    return array([ftheta, fomega], float)


part = str(input("what part would you like to print? (a or b) "))

r = array([179*pi/180, 0], float)
tpoints = arange(tmin, tmax, h)
thetapoints = []
omegapoints = []

for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    
    # now do some runge-kutta (p336)
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6


if part in ['a']:
    figure(1)
    clf()
    title("theta(t)")
    plot(tpoints, thetapoints)
    xlabel("t")
    ylabel("theta")


if part in ['b']:
    scene = canvas(width = 500, height = 500, center = vector(0,0,0), background = color.black)
    
    # sphere with radius of 5 cm
    bob = sphere(pos = vector(l,0,0), radius = 0.01, color = color.red)
    
    it = 0
    for t in arange(0,1e6,0.1):
        angle = thetapoints[it] - pi/2
        rate(60) # steps per second
        bob.pos = vector(l*cos(angle), l*sin(angle), 0)
        it = it + 1
