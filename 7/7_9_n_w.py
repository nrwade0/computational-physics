# -*- coding: utf-8 -*-
"""
Created on Fri May  4 21:28:42 2018

@author: nit_n
"""

from numpy import empty, loadtxt, log, exp
from numpy.fft import rfft2, irfft2
from pylab import plot, show, xlim, ylim, clf, figure, xlabel, ylabel, gray, imshow

sig = 25

x = loadtxt("blur.txt", float)
rows = x.shape[0]
cols = x.shape[1]

figure(1)
clf()
gray()
imshow(x)

f = empty([rows, cols], float)
g = empty([rows, cols], float)

for j in range(cols):
    jp = j
    if jp>cols/2:
        jp -= cols
        
    for i in range(rows):
        ip = i
        
        if ip>rows/2:
            ip -= rows
            
        f[i,j] = exp(-(ip**2 + jp**2)/(2*sig**2))
        g[i,j] = ip
        
figure(2)
clf()
imshow(log(f))

xfft = rfft2(x)
ffft = rfft2(f)

yfft = empty([rows,cols//2 + 1], complex)

for j in range(cols//2 + 1):
    for i in range(rows):
        yfft[i,j] = xfft[i,j]/max(ffft[i,j], 3e-4)

y = irfft2(yfft)

figure(3)
clf()
imshow(y)

print("Some coefficients that are less that a certain error, epsilon, are left alone.  This afflicts our ability to unblur every photo completely.")



