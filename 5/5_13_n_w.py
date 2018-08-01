# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 23:57:02 2018

Hermite polynomial function else return formula
https://stackoverflow.com/questions/40729019/write-a-recursive-function-to-find-hermite-polynomials

Making a list callable by changing () to []
https://stackoverflow.com/questions/5735841/typeerror-list-object-is-not-callable-while-trying-to-access-a-list

linspace documentation
https://docs.scipy.org/doc/numpy-1.12.0/reference/generated/numpy.linspace.html

@author: nit_n
"""


from pylab import plot, show, clf, title
from math import exp, sqrt, factorial, pi, tan, cos
from numpy import linspace, array
from gaussxw import gaussxwab


def H(n,x): # Hermite polynomial function
    if n < 0: # under 0
        return 0
    if n == 0: # n=0 case
        return 1
    if n == 1: # n=1 case
        return 2*x
    else: # otherwise subrtact a 1 from all n becauase we compute n not n+1
        return 2*x*H(n-1,x)-2*(n-1)*H(n-2,x)

   
def wave(n,x): # wave function
    one = 1/(sqrt(2**n*factorial(n)*sqrt(pi)))
    two = exp(-x*x/2)
    return H(n,x)*one*two


def f(n,z): # part c function for root-mean-squared
    return (tan(z)*tan(z)*abs(wave(n,tan(z)))**2)/cos(z)**2



part = input(str("Enter which part (a, b, or c): "))


if part in ['a']:
    clf    
    # array of colors iterated
    colors = array(['go', 'mo', 'ro', 'bo'])
   
    n = 0
    for n in range(4):
        x = linspace(-4, 4 , 100) # from -4 to 4 in 100 evenly spaced intervals
        for i in x:
            y = wave(n,i)
            plot(i, y, colors[n])
    title("part a: wave functions")
    show()


if part in ['b']: # too long!!!!
    clf
    n = 30
    x = linspace(-10, 10 , 50)
    for i in x:
        y = wave(n,i)
        plot(i, y, 'ko')
    show()


if part in ['c']:
    # rearrange to eqn 5.73 on p1 80
    n = 5
    
    N = 100
    a = -pi/2
    b = pi/2
    x,w = gaussxwab(N,a,b)
    s = 0.0
    
    for k in range(N):
        s += w[k]*f(n, x[k])
    
    print('uncertainty =', sqrt(s))
    print("given = 2.3")
