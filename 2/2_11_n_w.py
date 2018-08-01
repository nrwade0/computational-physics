# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:37:10 2018
2.11
@author: nrwade0
"""


# set higher recursion limit
import sys
from math import factorial

sys.setrecursionlimit(1500)

# variables - different for part c!!!!
n = 4
k = 2

# what part would you like to do
parta = 1
partb = 1
partc = 1


# binomial function
def binomial(n,k):
    if k == 0:
        return 1
    else:
        aa = int(n - k)
        numerator = factorial(n)
        denominator1 = factorial(k)
        denominator2 = factorial(aa)
        return int(numerator/(denominator1*denominator2))



# PART A binomial
if parta == 1:
    print("PART A, where n =",n,"and k =",k,"--- binomial coefficient is",binomial(n,k))



# PART B Pascal's triangle
if partb == 1:
    for n in range(10): # first 10 rows of triangle
        for k in range(n + 1): # cycle through each k for each line
           print(binomial(n, k), end=' ') # print coefficient -- 
           # end=' ' keeps the print from \n
        
        print() # print new line for each row
    
    

# PART C probability of coin toss
if partc == 1:    
# n is the number of tosses
# k is the number of times landed on heads

# print probability
    n = 100
    k = 60
    print("part a (exactly 60 heads):",binomial(n,k)/(2**n))
    
    total = 0
    # sum of all probabilities 60 or more
    for i in range(k,n+1):
        # debug print(i)
        total = total + binomial(n,i)/(2**n)
    print("part b (60 or more times):",total)
    













