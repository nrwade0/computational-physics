# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 17:06:32 2018
 
@author: nit_n
"""

from numpy import exp, linspace
from pylab import clf, plot, show


def f(x):
    return 5*exp(-x) + x - 5


accuracy = 1e-6
h = 6.63e-34
c = 3e8
kb = 1.38e-23 # boltzman constant
lamb = 502e-9

# always graph first to see what you're dealing with
xplot = linspace(0,20,100)
yplot = 5*exp(-xplot) + xplot - 5

clf()
plot(xplot,yplot)
show()

# dont make interval too small -- use graph!!!
# might converge to a local min instead of the global min
x1 = 0.01
x2 = 10.0

f1 = f(x1)
f2 = f(x2)

while x2 - x1 > accuracy:
    xp = 0.5*(x1 + x2)
    fxp = f(xp)
    
    if f1*fxp > 0:
        x1, f1 = xp, fxp
    else:
        x2, f2 = xp, fxp
        
x = 0.5*(x1 + x1)
b = h*c/(kb*x)
T = b/lamb

plot(x,b,'ro')
plot(0,0,'ro')
print("The displacement constant is", b, "Km")
print("The surface temperature of the Sun is", T, "K")