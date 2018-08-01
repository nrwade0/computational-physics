# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 13:35:52 2018
graph of y1 http://www.wolframalpha.com/input/?i=y%3Dtan(sqrt((1e-9)%5E2*(9.1094e-31)*x%2F(2*1.0545718e-34%5E2))),+x+from+0+to+20
@author: nit_n
"""

from pylab import plot, show, clf, xlabel, ylabel
from numpy import linspace, zeros, tan, sqrt

def f1(x):
    return tan(sqrt(w*w*m*x/(2*hbar*hbar)))

def f2(x):
    return sqrt((V - Eplot)/Eplot)

def f3(x):
    return -sqrt(Eplot/(V - Eplot))

# constants
w = 1e-9 # m
m = 9.1094e-31 #kg
V = 20 # eV
hbar = 1.0545718e-34 #m^2 kg / s

clf()

# 0 to 20 in eV
Eplot = linspace(0.0, 20.0, 20) # in eV

y1 = f1(Eplot)
y2 = f2(Eplot)
y3 = f3(Eplot)

plot(Eplot,y1,'r-')
plot(Eplot,y2,'b-')
plot(Eplot,y3,'g-')
xlabel("E (eV)")
ylabel("y")

# ------------------------------------------
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
    
    
xlabel("E")
ylabel("three quantities of y")
show()