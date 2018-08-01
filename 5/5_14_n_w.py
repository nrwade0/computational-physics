# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 16:53:56 2018

@author: nit_n
"""

from gaussxw import gaussxw
import pylab as py

G = 6.67e-11
m = 1
rho = 907*10/1000

def f(x, y, z):
    return (x**2 + y**2 + z**2)**(-3/2)

N = 100
x, w = gaussxw(N)

def force(z): # equations 5.61, 5.62
    a = -5
    b = 5
    
    xp = 0.5*(b - a)*x + 0.5*(b + a)
    yp = xp
    
    wp = 0.5*(b - a)*w
    s = 0
    
    for i in range(N): # equation 5.63
        for j in range(N):
            s += wp[i]*wp[j]*f(xp[i], yp[j], z)
        
    F = G*m*rho*s*z
    
    return F

z = py.linspace(0, 10, 50)
F = force(z)

py.clf()

py.plot(z, F)
py.xlabel("z (m)")
py.ylabel("Force (N)")
py.show()