# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:06:03 2018
scipy.fftpack documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.dct.html
orthogonal structure: https://stackoverflow.com/questions/14325795/scipys-fftpack-dct-and-idct
@author: nit_n
"""

from numpy import loadtxt
from numpy.fft import rfft, irfft
from pylab import plot, clf, figure, title
from scipy.fftpack import dct, idct

cutoff = 0.02

y = loadtxt("dow2.txt", float)

part = str(input("What part? (a or b) "))

if part in ['a']:    
    c1 = rfft(y)    
    n1 = int(cutoff*len(c1))    
    c1[n1:] = 0    
    y1 = irfft(c1)
    
    print("Using fft")
    print("black: plotted all data")
    print("blue: everything but first 2% cutoff")
    
    figure(1)
    clf()
    title("Using fft")
    plot(y, "k-")
    plot(y1, 'b-')

if part in ['b']:
    c1 = dct(y, norm='ortho')    
    n1 = int(cutoff*len(c1))    
    c1[n1:] = 0    
    y1 = idct(c1, norm='ortho')
    
    print("Using dcst")
    print("black: plotted all data")
    print("red: everything but first 2% cutoff")
    
    figure(1)
    clf()
    title("Using scipy dct")
    plot(y, "k-")
    plot(y1, 'r-')