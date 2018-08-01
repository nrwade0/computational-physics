# -*- coding: utf-8 -*-
"""
Created on Mon May 14 16:44:09 2018
done with small derivation for part a
@author: nit_n
"""

from numpy import sqrt, array, arange
from pylab import plot, xlim, clf, figure

G = 6.67e-11
M = 1.989e30
h0 = 1.0e5
tmax = 1.5e9
tmin = 0
delta = 1e3/(365.25*24*3600)
x0 = 4.0e12
y0 = 0.0
u0 = 0.0
v0 = 500.0
N = 1000

def f(r):
    x = r[0]
    y = r[1]
    
    u = r[2]
    v = r[3]
    
    fx = u
    fy = v
    
    fu = -G*M*x/(x**2 + y**2)**1.5
    fv = -G*M*y/(x**2 + y**2)**1.5
    
    return array([fx, fy, fu, fv], float)



part = str(input("what step size would you like? (fixed or adaptive) "))

r = array([x0, y0, u0, v0], float)
xpoints = []
ypoints = []


if part in ['fixed']:
    N = 1e5
    h = (tmax - tmin)/N
    
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
        
    figure(2)
    clf()
    plot(xpoints, ypoints, "k.")
    xlim(-0.5e12, 4.5e12)
    
    print("h =", h, " - any higher (lower N) causes shape not to be an ellipse")
    print("Fixed step size = longer running time.")
    print("Results are similar but do not look as clean as adaptive step size.")

###############################################

if part in ['adaptive']:
    
    h = h0    
    t = 0.0
    
    while t < tmax:
        
        k1 = 2*h*f(r)
        k2 = 2*h*f(r + 0.5*k1)
        k3 = 2*h*f(r + 0.5*k2)
        k4 = 2*h*f(r + k3)
        
        r1 = r + (k1 + 2*k2 + 2*k3 + k4)/6
        
        k1 = h*f(r)
        k2 = h*f(r + 0.5*k1)
        k3 = h*f(r + 0.5*k2)
        k4 = h*f(r + k3)
        
        r2 = r + (k1 + 2*k2 + 2*k3 + k4)/6
        
        k1 = h*f(r2)
        k2 = h*f(r2 + 0.5*k1)
        k3 = h*f(r2 + 0.5*k2)
        k4 = h*f(r2 + k3)
        
        r2 += (k1 + 2*k2 + 2*k3 + k4)/6
        
        dx = r1[0] - r2[0]
        dy = r1[1] - r2[1]
        
        # equation 8.53
        rho = 30*h*delta/sqrt(dx**2 + dy**2)
        
        if rho >= 1:
            
            t += 2*h
            
            h *= min(rho**0.25, 2.0)
            r = r2
            xpoints.append(r[0])
            ypoints.append(r[1])
            
        else:
            h *= rho**0.25
            
    figure(2)
    clf()
    plot(xpoints, ypoints, "k.")
    plot(xpoints, ypoints, "k-")
    xlim(-0.5e12, 4.5e12)
    
    print("Overall, much better than the fixed step size attempt.")
    