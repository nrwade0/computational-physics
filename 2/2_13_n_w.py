# -*- coding: utf-8 -*-
"""
2.13
nrwade0
Feb 26, 2018
"""

"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
"""

print("part a: Catalan numbers")

def catalan(n):
    if n==0:
        return 1
    else:
        return (4*n-2)/(n+1)*catalan(n-1)
 
n = int(input("what is n: "))
print(catalan(n))

# -------------------------------------------------------

print("")
print("part b: Euclidean algorithm")

def euclid(a,b):
    if b==0:
        return a
    else:
        return euclid(b,a%b)
    
a = int(input("first number (m): "))
b = int(input("second number (n): "))
print(euclid(a,b))