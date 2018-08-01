# -*- coding: utf-8 -*-
"""
Created on Fri May  4 21:28:42 2018

@author: nit_n
"""

from numpy import arange, array, sin, pi
from numpy.fft import rfft
from pylab import plot, xlim, clf, figure

N = 1000
part = str(input("Enter the part of the problem (a, b, or c): "))

if part in ['a']:
    
    # square wave function
    def f(x):
        if x < 0.5:
            return 1
        else:
            return -1
        
    x = arange(0, 1, 1/N)
    y = array(list(map(f,x)))
        
    c = rfft(y)
    
    # plot f(x)
    figure(1)
    clf()
    plot(x, y)
    
    # plot fourier coefficients
    figure(2)
    clf()
    plot(abs(c))
    
if part in ['b']:
    
    # sawtooth wave function
    y = arange(N)
    
    c = rfft(y)
    
    # plot f(x)
    figure(1)
    clf()
    plot(x, y)
     
    # plot fourier coefficients
    figure(2)
    clf()
    plot(abs(c))
    xlim(0,100)
    
if part in ['c']:
    
    # modulated sine wave function
    def f(x):
        return sin(pi*x)*sin(20*pi*x)
    
    x = arange(0, 1, 1/N)
    y = array(list(map(f,x))) 
    
    c = rfft(y)
       
    # plot f(x)
    figure(1)
    clf()
    plot(x, y)
    
    # plot the fourier coefficients
    figure(2)
    clf()
    plot(abs(c))
    xlim(0,100)
    