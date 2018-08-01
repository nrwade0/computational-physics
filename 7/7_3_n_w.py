# -*- coding: utf-8 -*-
"""
Created on Fri May  4 21:28:42 2018
part b: https://stackoverflow.com/questions/4225432/how-to-compute-frequency-of-data-using-fft
Equation for part b from link: frequency = sampling_rate*peak_k_value/length(fft)
piano keys frequency list: https://en.wikipedia.org/wiki/Piano_key_frequencies
@author: nit_n
"""

from numpy import loadtxt, zeros
from numpy.fft import rfft
from pylab import plot, xlim, ylim, figure, title

booms = loadtxt("piano.txt", float)
trumps = loadtxt("trumpet.txt", float)

part = str(input("what part? (a or b): "))

if part in ['a']:
    
    # note axis differences for both figures.
    # x, y lims were given to emphasize wave structure
    figure(1)
    plot(booms, 'k-')
    title("piano")
    xlim(-50, 3200)
    ylim(-20000, 20000)
    
    figure(2)
    plot(trumps, 'k-')
    title("trumpet")
    xlim(-50, 3200)
    ylim(-10000, 10000)

    # calculate rffts
    pianofft = rfft(booms)
    trumpetfft = rfft(trumps)
    
    plotpiano = zeros(10000)
    plottrumpet = zeros(10000)
    for i in range(10000):
        plotpiano[i] = abs(pianofft[i])
        plottrumpet[i] = abs(trumpetfft[i])
    
    figure(3)
    title("piano coefficients")
    plot(plotpiano, 'r-')
    
    figure(4)
    title("trumpet coefficients")
    plot(plottrumpet, 'b-')
    
    print("Conclusion: piano had one main frequency with less harmonics.")
    print("Trumpet was different in that it had many harmonics along with the fundamental frequency.")
    print("Neither had much white noise.")
    
if part in ['b']:
    k = 44100*1185/len(booms)
    print("k =", k, "Hz")
    print("C5, Tenor C (twice the frequency of middle C)")