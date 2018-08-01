# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:41:40 2018

@author: nit_n
"""

from numpy import zeros, empty, arange, sin
from banded import banded
from pylab import plot,show
from vpython import sphere, vector, canvas, color, rate

# constants
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 2.0
alpha = 2*k - m*omega**2

# set up the initial values of the arrays
A = empty([3,N], float)
A[0,:] = -k
A[1,:] = alpha
A[2,:] = -k
A[1,0] = alpha - k
A[1,N-1] = alpha - k
v = zeros(N, float)
v[0] = C

# solve the equations
x = banded(A,v,1,1)

"""
# make a plot using both dots and lines
plot(x)
plot(x,'ko')
show()
"""

scene = canvas(width = 500, height = 500, center = vector(0,0,0), background = color.white)

s = empty(N,sphere)

for n in range(N):
    s[n] = sphere(pos = vector(3*n*(-1)**n, x[n], 0), radius = 2, color = color.blue)

for t in arange(0,1e6,0.1):
    rate(1e3) # steps per second
    
    for n in range(N):
        s[n].pos = vector(3*n*(-1)**n, sin(t)*x[n], 0)

