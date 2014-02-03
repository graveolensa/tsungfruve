#!/usr/bin/python

from mpmath import *
import pylab

def newt(z):
    for i in range(1,30):
        z = z - (fp.zeta(z,1,1)-fp.zeta(z,1,0))/(fp.zeta(z,1,2)-fp.zeta(z,1,1))
    return z

fp.cplot(lambda z: newt(z), [-40,40], [-40,40], points=800000, verbose=True, file="zetesque.svg")
