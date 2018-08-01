# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:17:35 2018

@author: nit_n
"""

# import math
import math

# define some constants
G=6.67e-11 #big G
M=5.97e24 #mass of earth
R=6371e3 #radius of earth (e3 to convert to meters)
hi=math.pi #pi

"""
# different periods
Tgeo=86400      # 1 day
Tlow=5400       # 90 mins
Tverylow=2700   # 45 mins
Tside=86148     # sidereal day 23.93 hours
"""

# ask for input from user
T=float(input("Enter the period T: "))

# calculate h
h=((G*M*T**2)/(4*hi**2))**(1/3)-R

# output h
print("The value of h (meters) is ",h)
newh=h/(1e3)
print("kilometers: ",newh)