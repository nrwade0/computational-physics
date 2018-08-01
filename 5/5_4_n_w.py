# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:52:39 2018

@author: nit_n
"""

from numpy import sin,cos,pi,linspace,zeros,sqrt,log,seterr
from pylab import plot,xlabel,ylabel,legend,imshow,jet,show

# ignores the divide by zero error, works both ways
# seterr(divide='ignore', invalid='ignore')

n = 1000
a = 0
b = pi
h = (b-a)/n
lam = 500e-9
k = 2*pi/lam

def J(m,x):
    def f(theta):
        return cos(m*theta - x*sin(theta))
    
    s = f(a) + f(b) + 4*f(a + h)
    for k in range(1, n//2):
        s += 4*f(a + (2*k + 1)*h) + 2*f(a + 2*k*h)
    return h*s/3

part = str(input("enter the part of the problem: (a or b) " ))

if part in ['a']:
    x = linspace(0,20,n)

    plot(x, J(0,x), label = 'J0')
    plot(x, J(1,x), label = 'J1')
    plot(x, J(2,x), label = 'J2')
    
    xlabel('kr')
    ylabel('J (W^(1/2) m^(-1))')
    
    legend()
    show()

if part in ['b']:
    points = int(101)
    center = 50
    scale = 1e-6/center
    x = zeros([points, points])
    y = zeros([points, points])
    
    for i in range(0, points):
        x[:,i] = (i - center)*scale
        y[i,:] = (i - center)*scale
        
    r = sqrt(x**2 + y**2)
    bot = k*r
    I = (J(1, r*k)/(bot))**2
    
    log_I = log(I)
    
    jet()
    imshow(log_I)
    show()