# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:17:35 2018
2.6
@author: nit_n
"""

# import square root function
from math import sqrt

# givens
m=9.11e-31 # particle mass in kg
en=10 # kinetic in eV
pot=9 # potential in ev
hbar=1.05457e-34 # Plancks constant / 2 pi

# wavevector constants
k1=sqrt(2*m*en)/hbar
k2=sqrt(2*m*(en-pot))/hbar

# transmission and reflection probabilities
T=(4*k1*k2)/((k1+k2)**2)
R=((k1-k2)/(k1+k2))**2

# output
print("Transmission probability: ",T)
print("Reflection probability: ",R)

total=float(T+R)
print("total: ",total)