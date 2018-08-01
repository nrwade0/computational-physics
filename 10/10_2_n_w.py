# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:50:07 2018

@author: nrwade0
"""

from numpy import log, arange
from random import random
from pylab import plot, show, figure, clf, xlabel, ylabel, legend

N = int(1e4)

nBi = N
nTL = 0
nPb = 0
nstable = 0

tauBi = 46*60
tauTL = 2.2*60
tauPb = 3.3*60

pBi = log(2)/tauBi
pTL = log(2)/tauTL
pPb = log(2)/tauPb

ratioTL = 0.0209
ratioPb = 0.9791

tpoints = arange(0, 2e4, 1)
Bipoints = []
TLpoints = []
Pbpoints = []
stablepoints = []


for t in tpoints:
        
    for i in range(nPb):
        if random() < pPb:
            nPb = nPb - 1
            nstable = nstable + 1
            
    for i in range(nTL):
        if random() < pTL:
            nTL = nTL - 1
            nPb = nPb + 1
    
    for i in range(nBi):
        if random() < pBi:
            nBi = nBi - 1
            if random() < ratioTL:
                nTL = nTL + 1
            else:
                nPb = nPb + 1
                
    Bipoints.append(nBi)
    TLpoints.append(nTL)
    Pbpoints.append(nPb)
    stablepoints.append(nstable)

figure(1)
clf()
plot(tpoints, Bipoints, label='Bi')
plot(tpoints, TLpoints, label='Tl')
plot(tpoints, Pbpoints, label='Pb')
plot(tpoints, stablepoints, label='stable')
xlabel("t (s)")
ylabel("N")
legend()
show()