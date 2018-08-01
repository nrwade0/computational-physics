# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 17:59:47 2018
legend() documentation: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html
part e formula: https://en.wikipedia.org/wiki/Particle_in_a_box
line 71 printf options: https://stackoverflow.com/questions/2960772/how-do-i-put-a-variable-inside-a-string-in-python
@author: nit_n
"""

from math import pi, sin, sqrt
from numpy import empty, linspace
from numpy.linalg import eigvalsh
from pylab import show, plot, legend, clf


part = input(str("what part? (c, d, or e) "))

if part in ['c'] or ['e']:
    N = 10
    print("butt")
    
if part in ['d']:
    N = 100
    print("10 x 10 H array is accurate enough")
    
# define constants
hbar = 1.0546e-34
q = 1.6022e-19
M = 9.10094e-31
L = 5e-10
a = 10*q
to_print = 10

# function to return an element in matrix H
def H(m, n):
    if m == n:
        return (pi*m*hbar)**2/(2*L**2*M)+0.5*a
    
    if (m + n) % 2 == 0:
        return 0.0
    
    return -8*a*m*n/(pi**2*((m**2-n**2)**2))

# construct the matrix, note that m & n in these expressions are one less than
# in the original formulas because python numbering starts at 0, not 1
Hhat = empty([N, N])

for m in range(N):
    for n in range(N):
        Hhat[m, n] = H(m+1, n+1)
        
# calculate the values and the vectors
value = eigvalsh(Hhat)

# print the results
for n in range(to_print):
    print("E[", n+1, "] = ", value[n]/q, "eV")

if part in ['e']:
    
    clf
    colors = ['r-', 'g-', 'b-']
    wave = linspace(0, L, 100)
    x = linspace(0, L, 100)
    
    for n in range(3):
        # plot each wave function value for each i in x
        for i in range(len(wave)):
            kn = (n+1)*pi/L
            wave[i] = sin(x[i]*kn)*sqrt(2/L)/60000
            wave[i] = abs(wave[i])**2
        plot(x, wave, colors[n], label='n = %d'% (n+1))
    legend()
    show()
    
    