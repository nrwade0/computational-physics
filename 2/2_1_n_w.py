# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:17:35 2018

@author: nit_n
"""

g=9.81 #gravity

# input tower height meters
h=float(input("What is the height of the tower in meters "))

# calculate
t=(2*(h/g))**(1/2)

# round to the second decimal place
# https://docs.python.org/3.6/library/functions.html#round
tt=round(t,2)

# output time seconds
print("Time elapsed when object hits the ground is",tt,"seconds")