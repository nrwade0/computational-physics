# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 01:16:15 2018

math.log documentation
https://stackoverflow.com/questions/33754670/calculate-logarithm-in-python

scipy.special gamma function documentation
https://scipython.com/book/chapter-8-scipy/examples/the-gamma-function/

@author: nit_n
"""

from math import exp, log
from numpy import linspace, array
from pylab import plot, title, show, clf, xlabel, ylabel
from gaussxw import gaussxwab
from scipy.special import gamma


def gam(a,x): #the gamma function
    return x**(a-1)*exp(-x)

def badgamma(a): # gamma function where z = 1/2
    return exp((a-1)*log(1/2)+(1/2))


part = input(str("Enter which part (a, b, c, d, e, or f): "))


if part in ['a']:
    clf    
    # array of colors iterated
    colors = array(['ko', 'ko', 'go', 'ro', 'bo'])
   
    for a in range(2,5):
        x = linspace(0, 5 , 100)
        for i in x:
            y = gam(a,i)
            plot(i, y, colors[a])
    print("a=2: green | a=3: red | a=4: blue")
    title("part a: x^(a-1)*e^-x")
    xlabel("x")
    ylabel("gamma(x,a)")
    show()

if part in ['b']:
    print("see handout")
    
if part in ['c']:
    print("if c were replaced with x then z = x/(x+x) = 1/2")

if part in ['d']:
    print("see handout")
    
if part in ['e']:
    N = 125
    a = 0
    b = 1
    x,w = gaussxwab(N,a,b)
    s = 0.0
    A = 3/2
    
    for k in range(N): # using scipy.special gamma function "gamma"
        s += w[k]*gamma(A)
    
    print('gamma(3/2) =', s)
    print("given = 0.886")
    
if part in ['f']:
    print("2! = ",gamma(3), "| 5! = ",gamma(6), "| 9! = ",gamma(10))
    