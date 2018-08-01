# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 21:34:27 2018

@author: nit_n
"""

from numpy import array, empty


part = input(str("what part, a or b? "))

if part in ['a']:
    print("Equation 1:  4V1 - V2 - V3 - V4 = 5")
    print("Equation 2:  -V1 + 0V2 + 3V3 - V4 = 5")
    print("Equation 3:  -V1 + 3V2 + 0V3 - V4 = 0")
    print("Equation 4:  -V1 - V2 - V3 + 4V4 = 0")
    
if part in ['b']:
    
    # coefficients of equations
    A = array([[4, -1, -1, -1],
               [-1, 0, 3, -1],
               [-1, 3, 0, -1],
               [-1, -1, -1, 4]], float)
    
    # answers in equations
    v = array([-5, 5, 0, 0], float)
    N = len(v)
    
    # Gaussian elimination
    for m in range(N):
        
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