# -*- coding: utf-8 -*-
"""
2.9
@author: nrwade0
@version: 19.02.2018
"""

from math import sqrt

print("A value of 222 for L took about a minute for me.")

l=int(input("Max iterations (L>0): ")) # max iterations
r=range(-l,l+1)
m=0.0 # Madelung constant

for i in r:
    
    for j in r:
        
        for k in r:
            n=i+j+k   
            if n != 0:
                
                if n % 2 == 0:     
                    m+=1/sqrt(i**2+j**2+k**2)
                    
                else:   
                    m+=-1/sqrt(i**2+j**2+k**2)

print(m)