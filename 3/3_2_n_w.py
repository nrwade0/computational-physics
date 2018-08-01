# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 15:41:52 2018

@author: nit_n
"""

from math import cos,sin,pi
from pylab import plot,show,clf,xlim,ylim,xlabel,ylabel,title
from numpy import zeros,exp


parta = 0
partb = 0
partc = 0

print("Deltoid curve (part a), Galilean Spiral (part b), or Fey's function (part c)?")
part = str(input("Please input a, b, c or all: "))
if part in ['a']:
    parta = 1
if part in ['b']:
    partb = 1
if part in ['c']:
    partc = 1
if part in ['all']:
    parta = 1
    partb = 1
    partc = 1

clf


if parta == 1:
    # x and y data points saved in two seperate lists
    x = list()
    y = list()
    # cycle thru 200 hundred points between 0 and 2pi
    for i in range(201):
        # find angle between 0 and 2pi
        theta = i*pi/100
        # x value is calculated and appended
        x_temp = 2*cos(theta) + cos(2*theta)
        x.append(x_temp)
        # y value is calculated and appended
        y_temp = 2*sin(theta) - sin(2*theta)
        y.append(y_temp)
    # plot x,y as a blue line
    plot(x,y,'b-')
    xlim(-2,3.5)
    ylim(-3,3)
    xlabel("x")
    ylabel("y")
    title("Deltoid Curve")
    show()


if partb == 1:
    # r and theta data points saved in two seperate arrays
    r = zeros(1000,float)
    theta = zeros(1000,float)
    # cycle thru 99 hundred points between 0 and 10pi
    for i in range(0,1000):
        # theta value is calculated and appended
        theta_temp = i*pi/100
        theta[i] = theta_temp
        # r value is calculated and appended
        r_temp = theta[i]**2
        r[i] = r_temp
    
    # r and theta data points saved in two seperate arrays
    x = zeros(1000,float)
    y = zeros(1000,float)
    # convert back to cartesian coords
    for i in range(0,1000):
        x[i] = r[i]*cos(theta[i])
        y[i] = r[i]*sin(theta[i])
    
    # plot x, y as a green line
    plot(x,y,'g-')
    xlim(-900,1100)
    ylim(-1000,800)
    xlabel("x")
    ylabel("y")
    title("Galilean Spiral? (r=theta^2)")
    show()
    
    
if partc == 1:
    # r and theta data points saved in two seperate arrays
    r = zeros(24000,float)
    theta = zeros(24000,float)
    # cycle thru 100 points between 0 and 24pi
    for i in range(0,24000):
        # theta value is calculated and appended
        theta_temp = i*pi/2400
        theta[i] = theta_temp
        # r value is calculated and appended
        r_temp1 = exp(cos(theta[i]))
        r_temp2 = 2*cos(4*theta[i])
        r_temp3 = sin(theta[i]/12)**5
        r[i] = r_temp1 - r_temp2 + r_temp3
    
    # r and theta data points saved in two seperate arrays
    x = zeros(24000,float)
    y = zeros(24000,float)
    # convert back to cartesian coords
    for i in range(0,24000):
        x[i] = r[i]*cos(theta[i])
        y[i] = r[i]*sin(theta[i])
    
    # plot x, y as a green line
    plot(x,y,'r-')
    xlim(-3,5)
    ylim(-4,4)
    xlabel("x")
    ylabel("y")
    title("Fey's Function")
    show()
    
    
    
    
    
    
    
    
    
    
    
    