# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:38:36 2018

@author: nit_n
"""

from numpy import empty, zeros
from banded import banded
from pylab import plot, ylim

# define constants
N = 6
Vp = 5.0

# setup the arrays
A = empty([5,N], float)

A[0,:] = -1.0
A[1,:] = -1
A[2,:] = 4.0
A[3,:] = -1
A[4,:] = -1.0
A[2,0] = A[2, N-1] = 3.0

v = zeros(N, float)
v[0] = v[1] = Vp

# solve the equations
w = banded(A, v, 2, 2)

# make a plot
print(w)

plot(range(1, N+1), w)
plot(range(1, N+1), w, 'ko')
ylim(0,5)





