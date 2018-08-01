# -*- coding: utf-8 -*-
"""
Created on Tue May 22 15:25:39 2018

@author: nrwade0
"""

from numpy import sin, sqrt
from random import random

# constants
N = int(1e4)
count = 0

def f(x):
    return (sin(1/(x*(2-x))))**2

for i in range(N):
    x = 2*random()
    y = random()
    if y < f(x):
        count = count + 1
        
I = 2*float(count)/N
sigma = sqrt(I*(2 - I)/N)
print("the Monte Carlo method: ", I, sigma)

sum = 0.0
sumsq = 0.0

for i in range(N):
    fx = f(2*random())
    sum = sum + fx
    sumsq = sumsq + fx**2
    
mean = sum/N
var = sumsq/N - mean**2
I = 2*mean
sigma = 2*sqrt(var/N)

print("the mean value method: ", I, sigma)