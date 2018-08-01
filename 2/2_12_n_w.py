# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 00:37:10 2018
2.12
@author: nrwade0
"""

from math import sqrt

# start with prime number list of 2
prime = list()
prime.append(2)

beginning = 3
end = 10000

# cycle through each n from beginning to end
for n in range(beginning,end):
    
    # failed? yes or no
    failed = 'False'
    
    # cycle through each value in the current prime list
    for x in prime:
              
        # work up to the max limit
        if x >= sqrt(n):
            # too high
            failed == 'True'
        
        # if your current value, n, is divisble by a prime
        if n % x == 0:
            # then this is not a prime number and we break out immediately
            failed = 'True'
            # debug print("divisible failed")
            
    if failed == 'False':
        prime.append(n)
        # debug print("appended")
        
print(prime)