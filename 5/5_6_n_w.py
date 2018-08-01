# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 16:31:01 2018

@author: nit_n
"""

def f(x):
    return x**4 - 2*x + 1

# trapezoidal rule
N = 10
a = 0.0
b = 2.0
h = (b - a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a + k*h)
    
I1 = h*s
print("I1 =",I1)

# trapezoidal rule
N = 20
a = 0.0
b = 2.0
h = (b - a)/N

s = 0.5*f(a) + 0.5*f(b)
for k in range(1,N):
    s += f(a + k*h)
    
I2 = h*s
print("I2 =",I2)

epsilon = (1/3) * (I2 - I1)
print("epsilon [1/3 * (I2 - I1)] =", epsilon)
print("direct computation error (w/ 10 slices) =",4.4-I1)

"""
the two errors are different
epsilon is the error in step size increasing
direct computation error takes into account step size and rounding errors on the numerical method
"""