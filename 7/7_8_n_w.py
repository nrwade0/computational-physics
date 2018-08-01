# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:06:04 2018
Help: https://github.com/akels/ComputationalPhysics/blob/master/7.7.py
@author: nit_n
"""

from pylab import pi, sin, arange, sqrt, imshow, linspace, colorbar
from numpy.fft import fft

# define some constants
# transmission function
def q(u):
    return sin(alpha*u)**2

d = 20e-6 # slit distance meters
alpha = pi/d # constant in transmission function
w = 200e-6 # width of the grating meters
W = 10*w # bigger width of grating = 2 millimeters in meters
lam = 500e-9 # wavelength nanometers
f = 1 # focal length meters

# x values from 0 to 0.05 in 0.0025 increments (in centimeters)
x = linspace(0, .05, 250, endpoint=False)

# number of iterations
N = 1000

# array of intensity values (0 to 999)
n = arange(N)

# find each xk value, eliminating those outside of the "padded area"
# elimination done in line 40
u = n*W/N - W/2

# calculate w/ transmission function
y = sqrt(q(u))

# eliminates padded area to 0
y[abs(u)>w/2]=0

# calculate the signal coefficients
c = fft(y)

# calculate intensities
I = (abs(c)*W/N)**2

# density plot of intensity array
# 'aspect' changes height of plot
imshow((I[:200],),aspect=150)
colorbar()
