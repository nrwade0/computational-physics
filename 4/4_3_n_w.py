# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 21:13:18 2018

@author: nit_n
"""

def f(x):
    xandsome = x + delta
    d = (xandsome*(xandsome-1)-x*(x-1))/delta 
    return d
    
delta = 1e-2
truevalue = 2*(1)-1
print("true value: ",truevalue)
for i in range(7):
    approxderivative = f(1.0)
    print("delta =",delta, "| approximate derivative =",approxderivative)
    delta = delta / 1e2
    
"""
part a) the first two values do not agree because you are not infintely accurate.
    you are supposed to taek the limit as delta -> 0 but that is not what were doing here.
    we can only take delta to be very small.
    
part b) as delta decreases, derivative becomes more accurate
    after they truncate earlier, they will start to lose accuracy again from rounding.
"""