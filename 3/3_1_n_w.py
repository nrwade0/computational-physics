# -*- coding: utf-8 -*-
"""
3.1
nrwade0
March 12, 2018
"""

from pylab import show,plot,clf,xlim,ylim,xlabel,ylabel
from numpy import loadtxt,zeros

# load data
data = loadtxt("sunspots.txt",float)

# select part of exercise you wish to output
part = str(input("part a, b, or c? "))


# part a
if part in ['a']:
    x = data[:,0]
    y = data[:,1]
    clf()
    plot(x,y,"b-")
    xlim(-50,3200)
    ylim(-5,260)
    xlabel("Month since January 1749")
    ylabel("Sunspots (N)")
    show()


# part b
if part in ['b']:
    x = data[0:999,0] # rows 0 thru 999 and column 0
    y = data[0:999,1] # rows 0 thru 999 and column 1
    clf()
    plot(x,y,"b-")
    xlim(-10,1010)
    ylim(-5,250)
    xlabel("Month since January 1749")
    ylabel("Sunspots (N)")
    show()

    
# part c
if part in ['c']:
    x = data[0:999,0] # rows 0 thru 999 and column 0
    y = data[0:999,1] # rows 0 thru 999 and column 1
    n = (1000-5) // 11 # number of iterations (packs of averages)
    
    x_mean = zeros(n,float) # needs to be 5,16,27,38,49,60...
    y_mean = zeros(n,float)
    
    for i in range(0,n):
        x_mean[i] = 11 * i + 5
        y_sum = 0
        
        for j in range(11):
            k = j + i * 11
            y_sum += y[k]
        
        y_mean[i] = y_sum / 11
        
    
    clf()
    plot(x_mean,y_mean,"b-")
    xlim(-10,1010)
    ylim(-5,250)
    xlabel("Month since January 1749")
    ylabel("Sunspots (N)")
    show()