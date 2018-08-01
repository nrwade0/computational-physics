# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 20:59:43 2018

@author: nit_n
"""

from gaussxw import gaussxwab
from math import exp,pi


part = input(str("which part would you like? (a or b and c) "))

def f(z):
    return (z/(1-z))**3/(exp(z/(1-z))-1)*(1/(1-z)**2)

if part in ['a']:
    print("used Gaussian quadrature method because it is very accurate with a small number of sample points.")

if part in ['b and c']:
    N = 31
    a = 0.0
    b = 1.0
    x,w = gaussxwab(N,a,b)
    s = 0.0
    
    kb = 1.381e-23 # boltzmann constant
    T = 273.15 # temp in kelvin
    c = 3e8 # speed of light
    hbar = 6.626e-34/(2*pi) # reduced planck's constant
    
    jumble = (kb**4*T**4)/(4*pi**2*c**2*hbar**3)
    
    for k in range(N):
        s += w[k]*f(x[k])
        
    W = jumble*s
    print('integral =',s)
    print('constant (where T = 273.15 K) =',jumble)
    print("experimental =",W)
    print("actual = 314.661")
    
    sigma = 5.67e-8 # stefan-boltzmann constant
    sigmaalmost = W/(T**4)
    perc_diff = ((sigma-sigmaalmost)/sigma)
    print("----------------------")
    print("sigma experimental =",sigmaalmost)
    print("sigma actual =",sigma)
    print("percent difference =",perc_diff)