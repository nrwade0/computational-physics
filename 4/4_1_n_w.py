# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 17:37:10 2018
python arbitrary precision
@author: nit_n
"""

def factorial_int(n):
    n = int(n)
    if n==1:
        return 1
    else:
        return n*factorial_int(n-1)

def factorial_float(n):
    n = float(n)
    if n==1:
        return 1
    else:
        return n*factorial_float(n-1)    


print("integer 200!: ", factorial_int(200))
print("float 200!: ", factorial_float(200))

"""
Why?
python's arbitrary precision on integer values means it does not have a limit on integer values.
The same explanation does not hold true for floating-points
"""