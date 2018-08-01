# -*- coding: utf-8 -*-
"""
2.7
@author: nrwade0
Feb 23, 2018
"""

# Catalan numbers

n=1
c0=1
cn=0

while cn<=1e9: # while catalan numbers are less than one billion
    
    if cn==0: # first run thru
        print(c0) # print initial value
        cn=c0 # do not run this conditional again
    
    cnext=(4*n+2)/(n+2)*cn
    print(cnext)
    cn=cnext
    n=n+1
    