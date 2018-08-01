# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 20:08:27 2018

@author: nit_n
"""

from vpython import sphere,vector,color


part = str(input("NaCl crystal (part a) or face-centered cubic (part b)? (a or b) "))

parta = 0
partb = 0

if part in ['a']:
    parta = 1
if part in ['b']:
    partb = 1


if parta == 1:
    L=5
    R=0.3
    # determines whether next should be red or blue
    counter = 0
    
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if counter % 2 == 0:
                    sphere(pos=vector(i,j,k), radius=R, color=color.red)
                    counter += 1
                else:
                    sphere(pos=vector(i,j,k), radius=R, color=color.blue)
                    counter += 1
                    
    
    
if partb == 1:
    L=1
    R=0.3
    # determines whether next should be used or not
    counter = 0
    
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if counter % 2 == 0:
                    sphere(pos=vector(i,j,k), radius=R, color=color.green)
                    counter += 1
                else:
                    counter += 1
                    continue
                    