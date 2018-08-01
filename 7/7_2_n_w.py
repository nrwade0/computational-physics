# -*- coding: utf-8 -*-
"""
Created on Fri May  4 21:28:42 2018

@author: nit_n
"""

from numpy import loadtxt
from numpy.fft import rfft
from pylab import plot, xlim, ylim, clf, figure, xlabel, ylabel

data = loadtxt("sunspots.txt", float)
months = data[:, 0]
sunspots = data[:, 1]

figure(1)
clf()
plot(months, sunspots, 'b-')
xlim(-50, 3200)
ylim(-5, 260)
xlabel("Month since January 1749")
ylabel("Sunspots (N)")

c = rfft(sunspots)

figure(2)
clf()
plot(abs(c)**2)
xlim(0,40)
ylim(0,5e9)
ylabel("|ck|^2")

k = 24
month = len(months)/k

year = month/12

print(year)
