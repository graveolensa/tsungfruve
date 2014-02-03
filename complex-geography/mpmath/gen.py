#!/usr/bin/python

from mpmath import *
import pylab

def g(z):
    if((arg((z-j)/(z+j))>0)&(arg((z-j)/(z+j))<pi/4.0)):
        return z
    else:
        return 0.0


fp.cplot(lambda z: g(z), [-20,20], [-20,20], points=800000, verbose=True, file="plotset.png")
