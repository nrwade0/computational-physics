# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:37:10 2018

@author: nit_n
"""

from numpy import sqrt,pi,absolute
import time


def int_calc(n):
    
    h=2/n
    integral=0
    
    for i in range(1,n+1):
        x=-1+h*i
        y=sqrt(1-x**2)
        
        integral += h*y
    return integral

part = str(input("Enter the part of the problem, a or b: "))

if part in ['a']:
    I = int_calc(100)
    
    perc_diff = 100 * absolute((pi/2-I)*2/pi)
    
    print("The numerical value is ", I)
    print("The actual value is ", pi/2)
    print("The percent difference ", perc_diff)

if part in ['b']:
    
    t=0
    N=100
    
    while t<1:
        
        N=2*N
        
        t_start=time.time()
        I=int_calc(int(N))
        t=time.time() - t_start
    
    perc_diff = 100 * absolute((pi/2-I)*2/pi)
    
    print(N, "slices takes ", t,"seconds")
    print("The numerical value is ", I)
    print("The actual value is ", pi/2)
    print("The percent difference ", perc_diff)
