#!/usr/bin/python

from mpmath import *
import pylab

def g(q):
    out = 1.0;
    t=agm(1-q,1-q*q)
    if(abs(q)<1.0):
        for i in range(1,30):
            T = out * t
            t = agm(t, 1-q**(i+2))
        return out
    else:
        return 0.0

fp.cplot(lambda q: g(q), [-1.0,1.0], [-1.0,1.0], points=800000, verbose=True, file="agmestic.svg")        
