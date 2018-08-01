# -*- coding: utf-8 -*-
"""
Created on Mon May  7 17:49:17 2018

@author: nit_n
"""
from numpy import array, sin, cos, pi, sqrt, arange
from pylab import plot, clf, figure, xlabel, ylabel, ylim, xlim, title

g= 9.81
m = 1
rho = 1.22
c = 0.47
R = 0.08
h = 1e-3
theta = 30*pi/180
v0 = 100
const = rho*c*pi*R**2/(2*m)

def f(r):
    x = r[0]
    y = r[1]
    
    vx = r[2]
    vy = r[3]
    
    fx = vx
    fy = vy
    
    fvx = -const*vx*sqrt(vx**2 + vy**2)
    fvy = -const*vy*sqrt(vx**2 + vy**2) - g
    
    return array([fx, fy, fvx, fvy], float)

r = array([0, 0, v0*cos(theta), v0*sin(theta)])
xpoints = []
ypoints = []

while r[1] >= 0:
    
    # now do some runge-kutta (p336)
    k1 = h*f(r)
    k2 = h*f(r + 0.5*k1)
    k3 = h*f(r + 0.5*k2)
    k4 = h*f(r + k3)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6
    
    xpoints.append(r[0])
    ypoints.append(r[1])
    
figure(1)
clf()
plot(xpoints, ypoints)
xlabel("x")
ylabel("y")



m_range = arange(0.5, 5, 0.05)
x_dist = []

for m in m_range:
    r = array([0, 0, v0*cos(theta), v0*sin(theta)])
    xpoints = []
    ypoints = []
    const = rho*c*pi*R**2/(2*m)
    
    while r[1] >= 0:
        
        # now do some runge-kutta (p336)
        k1 = h*f(r)
        k2 = h*f(r + 0.5*k1)
        k3 = h*f(r + 0.5*k2)
        k4 = h*f(r + k3)
        
        r += (k1 + 2*k2 + 2*k3 + k4)/6
        
        xpoints.append(r[0])
        ypoints.append(r[1])
        
    x_dist.append(r[0])

figure(2)
clf()
plot(m_range, x_dist)
title("mass vs total distance")
xlabel("mass (kg)")
ylabel("distance (m)")
ylim(150, 550)
xlim(0.25, 5.25)

print("mass is less affected by air resistance, has higher kinetic energy")