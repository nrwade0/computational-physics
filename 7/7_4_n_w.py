# -*- coding: utf-8 -*-
"""
Created on Fri May  4 21:28:42 2018

@author: nit_n
"""

from numpy import loadtxt
from numpy.fft import rfft, irfft
from pylab import plot, clf, figure, title

cutoff1 = 0.1
cutoff2 = 0.02

y = loadtxt("dow.txt", float)

c1 = rfft(y)
c2 = rfft(y)

n1 = int(cutoff1*len(c1))
n2 = int(cutoff2*len(c2))

c1[n1:] = 0
c2[n2:] = 0

y1 = irfft(c1)
y2 = irfft(c2)

print("black: plotted all data")
print("red: everything but first 10% cutoff")
print("blue: everything but first 2% cutoff")

figure(1)
clf()
title("see command console for details")
plot(y, "k-")
plot(y1, 'r-')
plot(y2, 'b-')

print("When Fourier coefficients are set = 0, the plotted line seems less jagged and precise")
print("The more you cutoff, the more smooth the line looks.")