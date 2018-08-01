# -*- coding: utf-8 -*-
"""
Created on Mon May  7 18:07:04 2018
do part b
@author: nit_n
"""

import numpy as np
import pylab as pyl
import vpython as vis

N = 5
m = 1.0
k = 6.0
omega = 2.0

def f(r, t):
    xi = r[:N]
    nu = r[N:]
    
    fxi = np.empty(N, float)
    fnu = np.empty(N, float)
    
    fxi[0] = nu[0]
    fnu[0] = k*(xi[1] - xi[0]) + np.cos(omega*t)
    
    for i in range(1, N - 1):
        fxi[i] = nu[i]
        fnu[i] = k*(xi[i+1] - xi[i]) + k*(xi[i-1] - xi[i])
        
    fxi[N-1] = nu[N-1]
    fnu[N-1] = k*(xi[N-2] - xi[N-1])
    
    return np.concatenate([fxi, fnu])


part = str(input("what part would you like to output? (a or b) "))

a = 0.0
b = 20
n = 1000
h = (b - a)/n

r = np.zeros(2*N, float)
xipoints = np.empty([N, n], float)

for i in range(n):
    
    t = i*h
    
    xipoints[:, i] = r[:N]
    
    # now do some runge-kutta (p336)
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6

tpoints = np.arange(a, b, h)



if part in ['a']:
    pyl.figure(1)
    pyl.clf()
    for i in range(N):
        pyl.plot(tpoints, xipoints[i, :], label = 'm = %s kg' % float(i+1))
    pyl.xlabel("time")
    pyl.ylabel("displacement")
    pyl.ylim(-0.45, 0.82)
    pyl.legend()



if part in ['b']:
    scene = vis.canvas(width = 500, height = 500, center = vis.vector(0,0,0), background = vis.color.black)
        
    # sphere with radius of 5 cm
    mass = np.empty(6, vis.sphere)
    distance = np.array([-200, -100, 0, 100, 200])
    
    
    for i in range(N):
        mass[i] = vis.sphere(pos = vis.vector(distance[i],0,0), radius = 20, color = vis.color.blue)
    

    indexer = 0
    for t in np.arange(0, 1e6, 0.1):
        for i in range(N):
            
            vis.rate(115) # steps per second
            mass[i].pos = vis.vector(distance[i], 100*xipoints[i, indexer], 0) # x100 to emphasize the movement
            indexer += 1

