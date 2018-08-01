# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:07:03 2018

@author: nit_n
"""

from numpy import empty, array, arange
from pylab import plot, show, title, xlim

G = 6.67e-11
h0 = 1.0e5
delta = 1e3            # Required position accuracy per unit time (1 kilometer)

def f(r):
    x = r[0]
    y = r[1]
    
    u = r[2]
    v = r[3]
    
    fx = u
    fy = v
    
    fu = -G*M*x/(x**2 + y**2)**1.5
    fv = -G*M*y/(x**2 + y**2)**1.5
    
    return array([fx, fy, fu, fv], float)




part = str(input("what part would you like to do? (Earth (a) or Pluto (b)) "))



if part in ['a']: # EARTH
    M = 1.989e30           # mass of earth
    tmax = 3.154e7         # seconds in a year
    tmin = 0
    x0 = 1.4710e11         # perihelion distance
    y0 = 0.0
    u0 = 0.0
    v0 = 3.0287e4          # linear velocity
    N = 52                 # Number of "big steps" (7 days)
    H = (tmax - tmin)/N    # Size of "big steps" (week in seconds)

    
if part in ['b']: # PLUTO
    M = 1.31e22            # mass of pluto
    tmax = 7.81e9          # seconds in 248 years orbit
    tmin = 0
    x0 = 4.4368e12         # perihelion distance
    y0 = 0.0
    u0 = 0.0
    v0 = 6.1218e3          # linear velocity
    N = 52                 # Number of "big steps" (weeks)
    H = (tmax - tmin)/N    # Size of "big steps" (week in seconds)
    
    
tpoints = arange(tmin, tmax, H)
xpoints = []
ypoints = []
r = array([x0, y0, u0, v0], float)

# Do the "big steps" of size H
for t in tpoints:
    # show incrementation through tpoints
    print(t/tmax*100, "%")
    
    xpoints.append(r[0])
    ypoints.append(r[1])

    # Do one modified midpoint step to get things started
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)

    # The array R1 stores the first row of the
    # extrapolation table, which contains only the single
    # modified midpoint estimate of the solution at the
    # end of the interval
    R1 = empty([1, 4], float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))

    # Now increase n until the required accuracy is reached
    error = 2*H*delta
    while error > H*delta:

        n = n + 1
        h = H/n

        # Modified midpoint method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n - 1):
            r1 = r1 + h*f(r2)
            r2 = r2 +h*f(r1)

        # Calculate extrapolation estimates.  Arrays R1 and R2
        # hold the two most recent lines of the table
        R2 = R1
        R1 = empty([n, 4], float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
        
        for m in range(1 ,n):
            epsilon = (R1[m-1] - R2[m-1])/((n/(n-1))**(2*m) - 1)
            R1[m] = R1[m-1] + epsilon
        error = abs(epsilon[0])

    # Set r equal to the most accurate estimate we have,
    # before moving on to the next big step
    r = R1[n - 1]


if part in ['a']:
    
    # Plot the results
    title("EARTH Orbit")
    plot(xpoints, ypoints)
    plot(xpoints, ypoints,"b.")
    xlim(-1.75e11, 1.75e11)
    show()

if part in ['b']:
    # Plot the results
    title("PLUTO Orbit")
    plot(xpoints, ypoints)
    plot(xpoints, ypoints,"b.")
    show()
