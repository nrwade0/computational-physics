# -*- coding: utf-8 -*-
"""
2.8
nrwade0
Feb 23, 2018
"""

from numpy import array
a = array([1,2,3,4],int)
b = array([2,4,6,8],int)

# part a - every element has 3's in it
print("part a: ",b/a+1)

# part b - output: 2/2, 4/3, 6/4, 8/5
print("part b: ",b/(a+1))

# part c - output: 1/1, 1/2, 1/3, 1/4
print("part c: ",1/a)