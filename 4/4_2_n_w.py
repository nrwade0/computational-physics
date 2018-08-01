# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 19:53:43 2018

@author: nit_n
"""

import numpy as np

a = float(input("what is the value of a? "))
b = float(input("what is the value of b? "))
c = float(input("what is the value of c? "))


# PART A
determinant = b*b-4*a*c
print("determinant: ",np.sqrt(determinant))
print("b: ",b)

x1 = (-1*b + np.sqrt(determinant))/(2*a)
x2 = (-1*b - np.sqrt(determinant))/(2*a)
print("part a x1:",x1)
print("part a x2:",x2)

# PART B
x3 = (2*c)/(-1*b + np.sqrt(determinant))
x4 = (2*c)/(-1*b - np.sqrt(determinant))
print("part b x1:",x3)
print("part b x2:",x4)

"""
errors in computation comes from the fact that you are subtracting two numbers that
are extremely close to each other.  In this case, you have the determinant being 
just about = b (since 4*a*c is very small.)
"""

C = 1e-16
asigma = C*np.sqrt(x1*x1+x2*x2)
print("error in part a:",asigma)

bsigma = C*np.sqrt(x3*x3+x4*x4)
print("error in part a:",bsigma)




# https://en.wikipedia.org/wiki/Loss_of_significance#Instability_of_the_quadratic_equation
# https://codereview.stackexchange.com/a/103974
# depending on the sign in front of b will change the + or - sign in front of the determinant
# x1 = that numerator / 2a & x2 = c / (a*x1)
partc = str(input("do part c? (yes or no) "))

# PART C
if partc in ['yes']:
    determinant = b*b - 4*a*c
    error = 1e-8
    
    if b < 0:
        sup = (-1*b + np.sqrt(determinant))
    elif b > 0:
        sup = (-1*b - np.sqrt(determinant))
        
    x1 = sup/(2*a)
    x2 = c/(a*x1)
    
    print("x1 = ",x1)
    print("x2 = ",x2)
    