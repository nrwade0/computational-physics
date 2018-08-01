# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:20:32 2018

@author: nit_n
"""

from math import *
from pylab import *

def f(x):
    return 1 + 0.5*tanh(2*x)

h = 1e-3
x = linspace(-2, 2, 100)

numerical = (f(x + h) - f(x - h))/(2*h)
actual = 1 - tanh(2*x)**2

clf()
plot(x, actual, 'r', label = 'actual')
plot(x, numerical, 'bo', label = 'numerical')

legend()
show()