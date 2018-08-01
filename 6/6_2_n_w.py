# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 16:50:08 2018

@author: nit_n
"""

from numpy import array, empty

A = array([[2, 1, 4, 1],
           [3, 4, -1, -1],
           [1, -4, 1, 5],
           [2, -2, 1, 3]], float)

v = array([-4, 3, 9, 7], float)

N = len(v)

print("a and b in one swing...")

# go through the rows from m in range(N)
for m in range(N):
    
    # find row with largest pivot element
    pivot = m
    largest = A[m,m]
    
    for i in range(m+1, N):
        
        if abs(A[i, m]) > largest:
            largest = abs(A[i, m])
            pivot = i
    
    # swap rows
    for i in range(N):
        A[m, i], A[pivot, i] = A[pivot, i], A[m, i]
        
    v[m], v[pivot] = v[pivot], v[m]
    
    # gaussian elimination
    # divide by the diagonal element
    div = A[m, m]
    A[m, :] /= div
    v[m] /= div
    
    # subtract from lower rows
    for i in range(m+1, N):
        
        mult = A[i, m]
        A[i, :] -= mult*A[m, :]
        v[i] -= mult*v[m]
        
# back substitution
x = empty(N, float)
for m in range(N-1, -1, -1):
    x[m] = v[m]
    
    for i in range(m+1, N):
        x[m] -= A[m, i]*x[i]

print(x)






