# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:39:59 2018

@author: nit_n
"""


from numpy import arange
from pylab import plot, clf, figure, xlabel, ylabel

# define some constants
RC = 0.1
tstart = 0.0
tstop = 10.0
N = 1000

# basically a step function
def Vin(t):
    if int(2*t) % 2 == 0:
        return 1.0
    else:
        return -1.0

def f(vout, t):
    return (Vin(t) - vout)/RC



h = (tstop - tstart)/N
tpoints = arange(tstart, tstop, h)

# start with empty matrix and append values
vpoints = []
vout = 0.0

for t in tpoints:
    vpoints.append(vout)
    
    # now do some runge-kutta (p336)
    k1 = h*f(vout, t)
    k2 = h*f(vout + 0.5*k1, t + 0.5*h)
    k3 = h*f(vout + 0.5*k2, t + 0.5*h)
    k4 = h*f(vout + k3, t + h)
    
    vout += (k1 + 2*k2 + 2*k3 + k4)/6

figure(1)
clf()
plot(tpoints, vpoints)
xlabel("Time")
ylabel("Voltage")


print("Part B: A low-pass filter is a filter that passes signals with a frequency lower than a certain cutoff frequency and attenuates signals with frequencies higher than the cutoff frequency.")
print("Our graph simply shows that some of these frequencies are attenuated and others are filtered out.")









