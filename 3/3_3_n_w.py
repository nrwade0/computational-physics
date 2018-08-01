# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:54:27 2018

@author: nit_n
"""

from pylab import show,imshow,clf,xlabel,ylabel,jet,title,colorbar
from numpy import loadtxt

clf

data = loadtxt('stm.txt',float)

imshow(data,origin="lower",)
xlabel("x coordinate")
ylabel("y coordinate")
title("STM density map (height)")
jet()
colorbar()
show()