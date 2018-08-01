# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 21:56:17 2018
help: https://stackoverflow.com/questions/45377971/simple-mandelbrot-set-in-python
@author: nit_n
"""


from pylab import imshow,show,jet,colorbar
from numpy import zeros,linspace,log


N = 1000
max_iterations = 100

# creates map of N x N grid (x and y values)
data = zeros([N,N],int)

# two arrays of N evenly spaced intervals from -2 to 2
xcoords = linspace(-2,2,N)
ycoords = linspace(-2,2,N)

# enumerate function: https://docs.python.org/3/library/functions.html#enumerate
# see also: https://docs.python.org/2.3/whatsnew/section-enumerate.html
# saves iterator value in u and v
# saves coordinate value in x and y
for butts,x in enumerate(xcoords):
    for craps,y in enumerate(ycoords):
        
        # two complex numbers used
        # c becomes the coordinates evaluated
        z = complex(0,0)
        c = complex(x,y)
        
        # up to 100 iterations of calculation
        for iterations in range(max_iterations):
            
            # calculate from 0 and reuse in each iteration after
            z_prime = z**2 + c
            z = z_prime
            # if |z| is greater than 2, then you're done
            # save the number of iterations to the data map
            if abs(z) > 2.0:
                data[craps,butts] = iterations
                break

# output number of iterations on the grid
# use jet coloring scheme and display colorbar
imshow(data,origin="lower")
jet()
colorbar()
show()
