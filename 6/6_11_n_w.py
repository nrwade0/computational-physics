# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 18:04:46 2018
p 260
@author: nit_n
"""

from numpy import exp


part = input(str("What part would you like to do (a, b, c , or d)? "))

if part in ['a']:
    print("see derivation handout")
    
c = 2
accuracy = 1e-6

def f(x,c):
    return 1- exp(-c*x)

def df(x,c):
    return c*exp(-c*x)

x = 1
epsilon = 1 # eqn 6.83 p256 for part b and bototom of 260 part c
n = 0

if part in ['b']:
    while epsilon > accuracy:
        n = n + 1
        xp = f(x,c)
        epsilon = abs((xp-x)/(1-1/df(xp,c)))
        x = xp
        
    print("number of iterations (relaxed w = 0): ", n)

if part in ['c']:
    while epsilon > accuracy:
        w = 0.5 # overrelaxation method
        n = n + 1
        xp = (1 + w)*f(x,c) - w*x
        epsilon = abs((xp - x)/(1 - 1/(1 + w)*df(xp,c) - w))
        x = xp
        
    print("number of iterations (overrelaxed w = 0.5): ", n)

if part in ['d']:
    print("yes, w < 0 would be useful when we overshoot our value and we can restrict the relaxtion.")
    print("For a convergence that bounces over the actual value, this would help it converge fast onto it.")