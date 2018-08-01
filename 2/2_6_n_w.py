# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:17:35 2018
2.6
@author: nit_n
"""
# v1, l1 are perihelion points
# v2, l2 are aphelion points

# import square root function
from math import sqrt, pi

# constants
G=6.6738e-11 # m^3 kg^-1 s^-2
M=1.9891e30 # kg (mass of sun)

l1=float(input("Enter perihelion distance in meters: "))
v1=float(input("Enter perihelion speed in m/s: "))

# PART C ----------------------------------------------------
## Earth
l1=1.4710e11 # meters
v1=3.0287e4 # m/s

## Halley's comet
l1=8.7830e10 # meters
v1=5.4529e4 # m/s
# ------------------------------------------------------------

# quadratic parts for v2
a=1
b=(-2*G*M)/(l1*v1)
c=-(v1**2-(2*G*M)/l1)

# quadratic formula (+ and -)
v2_1=(-b+sqrt(b**2-4*a*c))/2*a
v2_2=(-b-sqrt(b**2-4*a*c))/2*a

# output part a block
print("PART A")
print("v2_1 =",v2_1,"m/s")
print("v2_2 =",v2_2,"m/s")

# answer to part a
print("Note v2 cannot equal v1 unless l1 = l2, so v2_2 is correct")
v2=v2_2
l2=l1*v1/v2

print("") # extra line

 # ------------------------------------------------------------------
print("PART C")

# define some terms
a=(l1+l2)/2 # semimajor axis
b=sqrt(l1*l2) # semiminor axis
T=(2*pi*a*b)/(l1*v1) # orbital period
e=(l2-l1)/(l2+l1) # orbital eccentricity

T=T/3600/24/365.25 # to put orbital period into years

print("semimajor axis:",a,"meters")
print("semiminor axis:",b,"meters")
print("orbital period",T,"years")
print("orbital eccentricity",e)