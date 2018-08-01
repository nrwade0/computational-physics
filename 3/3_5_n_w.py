# -*- coding: utf-8 -*-
"""
3.5
nrwade0
March 12, 2018
"""

from vpython import sphere,vector,canvas,color,rate
from numpy import arange,loadtxt,empty,array
from math import sin,cos,pi

# load planet data
data = loadtxt("planet_data.txt",float)

# part a
sun = data[6,0]

# mark 1
radius = data[:,0]
distance = data[:,1]
period = data[:,2]
colors = array([[0.5, 0.5, 0.5],[0,0,1],[0,1,0],[1,0,0],[1,0.5,0],[0,1,1]],float)

# mark 2

# parameters, scaling factors
w = 800
h = 800
c1 = 1.5e3
c2 = 5e1

part = str(input("Enter part of the problem, a or b: "))
scene = canvas(width = w, height = h, center = vector(0,0,0), background = color.black)


if part in ['a']:
    
    s_sun = sphere(pos = vector(0,0,0), radius = c2*sun, color = color.yellow)
    
    s = empty(6,sphere)
    
    for n in range(6):
        s[n] = sphere(pos = vector(distance[n],0,0), radius = c1*radius[n], color = vector(colors[n,0], colors[n,1], colors[n,2]))
      
if part in ['b']:
    
    s_sun = sphere(pos = vector(0,0,0), radius = c2*sun, color = color.yellow)
    
    s = empty(6,sphere)
    
    for n in range(6):
        s[n] = sphere(pos = vector(distance[n],0,0), radius = c1*radius[n], color = vector(colors[n,0], colors[n,1], colors[n,2]))
    
    for t in arange(0,1e6,0.1):
        rate(1e3) # steps per second
        
        for n in range(6):
            s[n].pos = vector(distance[n]*cos(2*pi*t/period[n]), distance[n]*sin(2*pi*t/period[n]),0)