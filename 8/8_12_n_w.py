# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:19:44 2018

@author: nit_n
"""

from numpy import array, arange, sqrt
from pylab import plot, figure, xlabel, clf, ylabel, legend, title

G = 6.67e-11
M = 1.9891e30
m = 5.9722e24

x0 = 1.521e11
y0 = 0.0

vx0 = 0.0
vy0 = 2.9291e4

a = 0.0
b = 50e6
h = 3600.0

def mag(r):
    return sqrt(sum(r*r))

def f(r):
    return -G*M*r/mag(r)**3

def V(r):
    return -G*M*m/mag(r)

def T(v):
    return 0.5*m*sum(v*v)


# initial value arrays
r = array([x0, y0],float)
v = array([vx0, vy0], float)

# equation 8.77
vhalf = v + 0.5*h*f(r)

# all plotting lists
tpoints = arange(a, b, h)
xpoints = []
ypoints = []
Vpoints = []
Tpoints = []
Epoints = []


for t in arange(a, b, h):
    
    # save plotting values
    xpoints.append(r[0])
    ypoints.append(r[1])
    Vpoints.append(V(r))
    Tpoints.append(T(v))
    Epoints.append(V(r) + T(v))
    
    # equation 8.78
    r = r + h*vhalf
    k = h*f(r)
    v = vhalf + 0.5*k
    vhalf = vhalf + k


figure(1)
clf()
title("Part A")
plot(xpoints, ypoints, 'k-')
xlabel("x")
ylabel("y")
print("Figure 1: orbit is visibly non-circular")

figure(2)
clf()
title("Part B")
plot(tpoints, Vpoints, "r", label = "PE")
plot(tpoints, Tpoints, "b", label = "KE")
plot(tpoints, Epoints, "g", label = "Total E")
xlabel("Time (s)") 
ylabel("Energy (J)")
legend()
print("Figure 2: PE and KE fluctuate but total E stays the same")

figure(3)
clf()
title("Part C")
plot(tpoints, Epoints, "k")
xlabel("Time (s)") 
ylabel("Energy (J)")
print("Figure 3: Total E always returns to it's initial point.  This is possible due to the Verlet method.")