# -*- coding: utf-8 -*-
"""
Created on Wed May  9 22:50:38 2018

@author: nit_n
"""


from numpy import array, arange
from pylab import figure, clf, plot, xlabel, legend, show, ylim, title


alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

tstart = 0.0
tstop = 30.0
N = 1000

# rabbits
def f(r, t):
    x = r[0]
    y = r[1]
    rabbit = alpha*x - beta*x*y
    fox = gamma*x*y - delta*y
    return array([rabbit, fox], float)
    

# start with empty matrix and append values
h = (tstop - tstart)/N
tpoints = arange(tstart, tstop, h)

xpoints = []
ypoints = []

# initial population conditions
r = array([2, 2], float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    
    # now do some runge-kutta (p336)
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6
    
figure(1)
clf()
plot(tpoints, xpoints, label='rabbit population')
plot(tpoints, ypoints, label='fox population')
xlabel("time")
ylim(0, 8.5)
legend(loc='upper left')
title("Lotka-Volterra equations")
show()

print("Figure 1 shows the population changes of rabbits and foxes in a system.  We can see that when the fox population is low, about t=1.5, that the rabbit poulation has a huge increase in size.")
print("Likewise, we see that the fox population begins to increase when the rabbit population is at it's peak, about t=2.7.")