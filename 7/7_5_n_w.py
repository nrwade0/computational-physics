# -*- coding: utf-8 -*-
"""
Created on Fri May  4 21:43:27 2018
square wave function: https://stackoverflow.com/questions/34121147/creating-an-array-for-values-of-a-square-wave-function
@author: nit_n
"""

from numpy import linspace, zeros
from pylab import plot
from numpy.fft import rfft, irfft

def f(t):
    if int(2*t)%2 == 0:
        return 1
    else:
        return -1

N = 1000

t_samples = linspace(0.0, 1.0, N, endpoint=False)

samples = zeros(N)
for i in range(N):
    samples[i] = f(t_samples[i])

plot(t_samples, samples, 'k-')

# calculate the fourier coefficients
fft = rfft(samples)

# remove all but the first 10 coefficients
fft[10:N] = 0

# turn back into signal
samples2 = irfft(fft)

plot(t_samples, samples2, 'r-')

print("black: original square wave signal")
print("red: inverse, artifact-ridden square wave signal")
print("This is due to the compression aspect in fast Fourier transforming")
print("Setting most Fourier coefficients to 0 emphasizes the impact that compression can have on a signal.")
print("Most sound/image/video files go through this problem but not as severe.")