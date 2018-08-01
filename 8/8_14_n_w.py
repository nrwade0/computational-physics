# -*- coding: utf-8 -*-
"""
Created on Mon May 14 17:49:32 2018

@author: nit_n
"""

from numpy import array, arange, sqrt, linspace
from pylab import plot, figure, clf, xlim, ylim, xlabel, ylabel, title, legend

m = 9.1094e-31
hbar = 1.0546e-34
e = 1.6022e-19
a = 1e-11
V0 = 50*e
w = 10*a
N = 1000
h = 2*w/N
anharmonic = False

def Vhar(x):
    return V0*(x/a)**2

def V(x):
    return V0*(x/a)**4

def f(r, x, E):
    psi = r[0]
    phi = r[1]
    
    fpsi = phi
    
    if anharmonic == True:
        fphi = (2*m/hbar**2)*(V(x) - E)*psi
    else:
        fphi = (2*m/hbar**2)*(Vhar(x) - E)*psi

    return array([fpsi, fphi], float)

def solve(E):
    psi = 0.0
    phi = 1.0
    
    r = array([psi, phi], float)
    
    psipoints = [psi]
    for x in arange(-w, w, h):
        k1 = h*f(r, x, E)
        k2 = h*f(r + 0.5*k1, x + 0.5*h, E)
        k3 = h*f(r + 0.5*k2, x + 0.5*h, E)
        k4 = h*f(r + k3, x + h, E)
        
        r += (k1 + 2*k2 + 2*k3 + k4)/6
        
        psipoints.append(r[0])
        
    return array(psipoints, float)

def boundary(E):
    psi = solve(E)
    return psi[N]

def secant(E1, E2):
    psi2 = boundary(E1)
    target = e/1000
    
    while abs(E1 - E2) > target:
        psi1, psi2 = psi2, boundary(E2)
        E1, E2 = E2, E2 - psi2*(E2 - E1)/(psi2 - psi1)
        
    return E2

def waveplot(E, lab):
    psi = solve(E)
    halfpsi = psi[0:N//2 + 1]
    
    integral = 2*h*(sum(halfpsi[1:N//2 - 1]**2) + 0.5*halfpsi[0]**2 + 0.5*halfpsi[N//2]**2)
    
    x = linspace(-w, w, N + 1)
    
    psi /= sqrt(integral)
    
    plot(x, psi, label = lab)

print("For the harmonic oscillator")
E1 = secant(0*e, 10*e)
print("E1 =", E1/e, "eV")
E2 = secant(500*e, 510*e)
print("E2 =", E2/e, "eV")
E3 = secant(1000*e, 1010*e)
print("E3 =", E3/e, "eV")

anharmonic = True
print("")

print("For the anharmonic oscillator")
E1 = secant(0*e, 10*e)
print("E1 =", E1/e, "eV")
E2 = secant(500*e, 510*e)
print("E2 =", E2/e, "eV")
E3 = secant(1000*e, 1010*e)
print("E3 =", E3/e, "eV")

figure(1)
clf()
waveplot(E1, "E1")
waveplot(E2, "E2")
waveplot(E3, "E3")
xlim(-5*a, 5*a)
ylim(-2.5e5, 2.5e5)
title("Anaharmonic Oscillator")
xlabel("x (m)")
ylabel("E (J)")
legend()