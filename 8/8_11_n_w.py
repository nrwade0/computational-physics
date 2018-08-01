# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:21:25 2018
HELP FROM:
https://www.youtube.com/watch?v=GzYrq49IgeQ
http://physics.bu.edu/~py502/lectures3/cmotion.pdf
https://en.wikipedia.org/wiki/Leapfrog_integration
http://phycomp.technion.ac.il/~david/thesis/node34.html
http://www.wolframalpha.com/widgets/view.jsp?id=e602dcdecb1843943960b5197efd3f2a
@author: nit_n
"""

# imports
from numpy import arange
from pylab import plot, show, figure, clf, xlabel, ylabel

# starting values
h = 0.001
tmax = 50.0
tmin = 0.0
N = 50000

def f(x, v): # returns acceleration (technically)
    # x = x(t)
    # v = dx/dt
    return v*v - x - 5
    

# plotted points
xpoints = []
tpoints = arange(tmin, tmax, h)

# initial values
x = 1.0
v = 0.0

vhalf = v + 0.5*h*f(x, v)

for t in tpoints: 
    
    # save x value
    xpoints.append(x)
    
    # leapfrog method
    x = x + h*vhalf
    k = h*f(x, v)
    v = vhalf + 0.5*k
    vhalf = vhalf + k
    
# plot
figure(1)
clf()
plot(tpoints, xpoints, 'r-')
xlabel("time")
ylabel("xpoints")
show()