# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:38:21 2018

@author: nrwade0
"""

from random import randrange

# constants
N = int(1e6)
count = 0


for i in range(N):
    
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    
    if dice1 == 6 & dice2 == 6:
        count = count + 1
        
print("Double six fraction = ", count/N)
print("for comparison 1/36 = ", 1/36)

