# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:52:58 2018

@author: nit_n
"""

from math import sqrt

part = input(str("what part would you like to do (a, b, or c)? "))


if part in ['a']:
    print("see derivation sheet")
    
if part in ['b']:
    
    # functions f and g, where a = 1 and b = 2
    def f(x,y):
        return y*(1 + x*x)
    def g(x,y):
        return 2/(1 + x*x)
    
    # counter, starting x and y values
    n = 0
    x = 1
    y = 1
    
    print("see derivation sheet")
    while n < 5:
        n = n + 1
        xp = f(x,y)
        x = xp
        yp = g(x,y)
        y = yp
        print("n =", n)
        print("x =", x)
        print("y =", y)
        print("------------------------")
        
    print("does not converge")
    
if part in ['c']:    
    
# functions f and g, where a = 1 and b = 2
    def f(x,y):
        return sqrt((2 - y)/y)
    def g(x,y):
        return x/(1 + x*x)
    
    # counter, starting x and y values
    n = 0
    x = 1
    y = 1
    
    while n < 40:
        n = n + 1
        xp = f(x,y)
        x = xp
        yp = g(x,y)
        y = yp
        print("n =", n)
        print("x =", x)
        print("y =", y)
        print("------------------------")
        
    print("actual: x = 2, y = 0.4")
    
    
    
    
    