# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 17:45:40 2018

@author: nit_n
"""
from math import *
from numpy import *
from pylab import *


#part = str(input("enter the part of the problem, a and b, or c: "))

#if part in ['a and b']:
w = loadtxt('altitude.txt',float)
h = 30e3

#if part in ['c']:
#    w = loadtxt('stm.txt',float)
#    h = 2.5
    

print(1)
phi = 45

row = len(w[:,1])
col = len(w[1,:])

diff_x = zeros([row, col])
diff_y = zeros([row, col])


for i in range(2, col - 2):
    # derivative of all values in left column two data points to one data point
    diff_x[:,i] = ((w[:, i - 2] - w[:, i + 2])/12 + (w[:, i + 1] - w[:, i - 1])/3)/h
    
# central difference derivative
diff_x[:,1] = (w[:, 2] - w[:, 0])/(2*h)
diff_x[:,col - 2] = (w[:, col - 1] - w[:, col - 3])/(2*h)


diff_x[:,0] = (w[:, 1] - w[:, 0])/h
diff_x[:,col - 1] = (w[:, col - 1] - w[:, col - 2])/h



for i in range(2, row - 2):
    # derivative of all values in left column two data points to one data point
    diff_y[i,:] = ((w[i-2,:] - w[i+2,:])/12 + (w[i+1,:] - w[i-1,:])/3)/h
    
# central difference derivative
diff_y[1,:] = (w[2,:] - w[0,:])/(2*h)
diff_y[row-2,:] = (w[row-1,:] - w[row-3,:])/(2*h)


diff_y[0,:] = (w[1,:] - w[0,:])/h
diff_y[row-1,:] = (w[row-1,:] - w[row-2,:])/h

diff_y = -diff_y

I = -(cos(phi*pi/180)*diff_x + sin(phi*pi/180)*diff_y)/sqrt(diff_x**2 + diff_y**2 + 1)


clf()
jet()
imshow(I)
colorbar()









