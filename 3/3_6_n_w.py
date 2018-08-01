# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:08:33 2018

@author: nit_n
"""

"""
I used 0.1 iterations to check if my code correctly outputted it.  It takes too long with that many iterations.  Below is one that
I found online that runs it very well.

a) A fixed point would look like a fixed point on the Feigenbaum plot. (probably from 1.0 - 3.0)
   A limit cycle would alternate from a few different values (3.0 - 3.5)
   Chaos would have no obvious pattern to it (3.5 - 4.0)
   
b) At 3.5 it moves from orderly behavior to chaotic behavior.
"""

from pylab import show,plot
from numpy import arange 

# beginning x value
x = .5

xplot = list()
rplot = list()

# iterative map
for r in arange(1,4,0.1):
    print(r)
    for i in range(1,1000):
        x_prime = r*x*(1-x)
        x = x_prime
        rplot.append(r)
        xplot.append(x_prime)
        plot(rplot,xplot,'ko')
        
    rplot.clear()
    xplot.clear()
    
show()


"""
# from: https://www.sophysics.co.uk/images/python/logistic_map.txt
# runs much faster!!!!

from pylab import show, scatter, xlabel, ylabel
from numpy import arange

def logistic(r,x):
    return r*x*(1-x)

for r in arange(1,4,0.01):
    xplot = []
    rplot = []
    i = 0
    x = 0.5
    while i < 1000:
        x = logistic(r,x)
        i = i + 1
    while i < 2000:
        x = logistic(r,x)
        i = i + 1
        xplot.append(x)
        rplot.append(r)
    scatter(rplot, xplot)
xlabel("r")
ylabel("x")
show()
"""