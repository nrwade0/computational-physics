# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:52:39 2018

@author: nit_n
"""

from numpy import absolute, empty, size, array

trap = [4.50656, 4.40107, 4.40001]

a = 0
b = 2

def f(x):
    return x**4 - 2*x + 1

part = str(input("enter the part of the problem: (a and b or c)" ))

if part in ['a and b']:
    n = 10
    h = (b - a)/n
    s = f(a) + f(b) + 4*f(a + h)
    
    for k in range(1, n//2):
        s += 4*f(a + (2*k + 1)*h) + 2*f(a + 2*k*h)
        
    integral = h*s/3
    error = absolute(integral - 4.4)/4.4
    print("the value of the integral is {} with a fractional error of {}." .format(integral, error))
    
if part in ['c']:
    n = [10, 100, 1000]
    integral = empty(3)
    error = empty(3)
    
    for i in range(0, size(n)):
        h = (b - a)/n[i]
        s = f(a) + f(b) + 4*f(a + h)
        
        for k in range(1, n[i]//2):
            s += 4*f(a + (2*k + 1)*h) + 2*f(a + 2*k*h)
            
        integral[i] = h*s/3
        error[i] = absolute(integral[i] - 4.4)/4.4
    
    print("the value of the integral is {} with a fractional error of {}." .format(integral, error))
    print("this compares with the trapezoidal rule as follows:")
    print(array([n, trap, integral], float))

