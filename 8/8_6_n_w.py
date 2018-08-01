# -*- coding: utf-8 -*-
"""
Created on Sat May 12 16:26:03 2018
derivation of equations of motion: https://physics.stackexchange.com/questions/57801/projectile-motion-with-drag?rq=1
@author: nit_n
"""

from numpy import array, arange
from pylab import plot, clf, figure, xlabel, ylabel, title

omega = 1
tmin = 0.0
tmax = 50.0
N = 1000
h = (tmax - tmin)/N

def f(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -omega*omega*x
    return array([fx, fy], float)


part = str(input("what part would you like to print? (a, b, c, d, or e) "))

if part in ['a']:
    r = array([1, 0], float)

if part in ['b']:
    r = array([2, 0], float)


tpoints = arange(tmin, tmax, h)
xpoints = []
ypoints = []

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    
    # now do some runge-kutta (p336)
    k1 = h*f(r, t)
    k2 = h*f(r + 0.5*k1, t + 0.5*h)
    k3 = h*f(r + 0.5*k2, t + 0.5*h)
    k4 = h*f(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6

if part in ['a']:
    figure(1)
    clf()
    title("PART A: x(t) w/ x(0) = 1")
    plot(tpoints, xpoints)
    xlabel("t")
    ylabel("x")

if part in ['b']:
    figure(2)
    clf()
    title("PART B: x(t) w/ x(0) = 2")
    plot(tpoints, xpoints)
    xlabel("t")
    ylabel("x")


# theta must be in radians for numpy.sin
def fc(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = -omega*omega*x*x*x
    return array([fx, fy], float)


if part in ['c']:
    r = array([1, 0], float)
    
if part in ['d']:
    r = array([2, 0], float)

tpoints = arange(tmin, tmax, h)
xpoints = []
ypoints = []

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    
    # now do some runge-kutta (p336)
    k1 = h*fc(r, t)
    k2 = h*fc(r + 0.5*k1, t + 0.5*h)
    k3 = h*fc(r + 0.5*k2, t + 0.5*h)
    k4 = h*fc(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6

if part in ['c']:
    figure(3)
    clf()
    title("PART C: phase space plot w/ x(0) = 1")
    plot(tpoints, xpoints)
    xlabel("position")
    ylabel("velocity")
    
if part in ['d']:
    figure(4)
    clf()
    title("PART D: phase space plot w/ x(0) = 2")
    plot(tpoints, xpoints)
    xlabel("position")
    ylabel("velocity")


########################################################## van der pol oscillator
def fr(r,t):
    x = r[0]
    y = r[1]
    fx = y
    fy = mu*(1 - x*x)*y - omega*omega*x
    return array([fx, fy], float)


if part in ['e']:
    r = array([1, 0], float)

########################################################### mu = 1
mu = 1
tpoints = arange(tmin, 20.0, h)
xpoints = []
ypoints = []

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    
    # now do some runge-kutta (p336)
    k1 = h*fr(r, t)
    k2 = h*fr(r + 0.5*k1, t + 0.5*h)
    k3 = h*fr(r + 0.5*k2, t + 0.5*h)
    k4 = h*fr(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6

if part in ['e']:
    figure(5)
    clf()
    title("PART E: van der Pol w/ mu = 1")
    plot(tpoints, xpoints)
    xlabel("position")
    ylabel("velocity")

############################################### mu = 2 plot

mu = 2
tpoints = arange(tmin, 20.0, h)
xpoints = []
ypoints = []

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    
    # now do some runge-kutta (p336)
    k1 = h*fr(r, t)
    k2 = h*fr(r + 0.5*k1, t + 0.5*h)
    k3 = h*fr(r + 0.5*k2, t + 0.5*h)
    k4 = h*fr(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6

if part in ['e']:
    figure(6)
    clf()
    title("PART E: van der Pol w/ mu = 2")
    plot(tpoints, xpoints)
    xlabel("position")
    ylabel("velocity")

##################################### mu = 4 plot

mu = 4
tpoints = arange(tmin, 20.0, h)
xpoints = []
ypoints = []

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    
    # now do some runge-kutta (p336)
    k1 = h*fr(r, t)
    k2 = h*fr(r + 0.5*k1, t + 0.5*h)
    k3 = h*fr(r + 0.5*k2, t + 0.5*h)
    k4 = h*fr(r + k3, t + h)
    
    r += (k1 + 2*k2 + 2*k3 + k4)/6

if part in ['e']:
    figure(7)
    clf()
    title("PART E: van der Pol w/ mu = 4")
    plot(tpoints, xpoints)
    xlabel("position")
    ylabel("velocity")












