# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 13:27:13 2018

@author: nit_n
"""

from numpy.linalg import solve
from numpy import array

part = input(str("solve problem 1 or 2? "))

if part in ['1']:
    
    A = array([[4, -1, -1, -1],
               [-1, 0, 3, -1],
               [-1, 3, 0, -1],
               [-1, -1, -1, 4]], float)
    
    v = array([-5, 5, 0, 0], float)
    
    x = solve(A, v)
    
    print(x)
    print("correct")
    
if part in ['2']:
    
    A = array([[2, 1, 4, 1],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)
    
    v = array([-4, 3, 9, 7], float)
    
    x = solve(A, v)
    
    print(x)
    print("correct")