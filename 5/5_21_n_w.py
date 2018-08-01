# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 01:16:27 2018

@author: nit_n
"""

from math import pi, sqrt, sin
from numpy import zeros
from pylab import imshow, jet, colorbar, show, clf, hsv


def chargedensity(x,y):
    return 100*sin(2*pi*x/10)*sin(2*pi*y/10)

field = zeros((11,11))
row = len(field[:,0])
col = len(field[0,:])

q1 = -1
q2 = 1

k = 1/(4*pi*8.854e-12)

for i in range(row):
    for k in range(col):
        
        # distances to point charges
        # r1 coords are (4.5, 5.0)
        # r2 coords are (5.5, 5.0)
        r1 = sqrt((4.5-i)**2+(5.0-k)**2)
        r2 = sqrt((5.5-i)**2+(5.0-k)**2)
        field[i,k] = (q1*k/r1) + (q2*k/r2)
   
    
part = input(str("Enter which part (a, b, or c): "))

if part in ['a']:
    clf()
    imshow(field, origin = 'lower')
    jet()
    colorbar()
    show()
    
if part in ['b']:
    h = 1e-3
    
    pdiff_x = zeros((row, col))
    pdiff_y = zeros((row, col))

    
    for i in range(2, 9):
        # derivative of all values in left column two data points to one data point
        pdiff_x[:,i] = ((field[:, i - 2] - field[:, i + 2])/12 + (field[:, i + 1] - field[:, i - 1])/3)/h
    
    # central difference derivative
    pdiff_x[:,1] = (field[:, 2] - field[:, 0])/(2*h)
    pdiff_x[:,col - 2] = (field[:, col - 1] - field[:, col - 3])/(2*h)
    
    
    pdiff_x[:,0] = (field[:, 1] - field[:, 0])/h
    pdiff_x[:, col - 1] = (field[:, col - 1] - field[:, col - 2])/h
    
    
    
    for i in range(2, 9):
        # derivative of all values in left column two data points to one data point
        pdiff_y[i,:] = ((field[i - 2,:] - field[i + 2,:])/12 + (field[i + 1,:] - field[i - 1,:])/3)/h
        
    # central difference derivative
    pdiff_y[1,:] = (field[2,:] - field[0,:])/(2*h)
    pdiff_y[row - 2,:] = (field[row - 1,:] - field[row - 3,:])/(2*h)
    
    
    pdiff_y[0,:] = (field[1,:] - field[0,:])/h
    pdiff_y[row - 2,:] = (field[row - 1,:] - field[row - 2,:])/h
    
    plot = input(str("which plot would you like outputted? (magnitude or direction) "))
    
    if plot in ['magnitude']:
        magfield = zeros((11,11))
        
        for i in range(0,11):
            for k in range(0,11):
                magfield[i,k] = sqrt(pdiff_x[i,k]**2 + pdiff_y[i,k]**2)
        
        clf()
        imshow(magfield, origin = 'lower')
        jet()
        colorbar()
        show()
        
    if plot in ['direction']:
        clf()
        imshow(field, origin = 'lower')
        hsv()
        colorbar()
        show()
    
if part in ['c']:
    
    L = 10 # cm
    field = zeros((11,11))
    
    for i in range(0,11):
        for k in range(0,11):
            field[i,k] = chargedensity(i,k)
    
    clf()
    imshow(field, origin = 'lower')
    jet()
    colorbar()
    show()
    
    
    
    
    