#!/usr/bin/python

from mpmath import *
import pylab

c = -0.726895347709114071439+0.188887129043845954792*j

def julia(z):
    for p in range(1,30):
        z = z*z + c
    return z

fp.cplot(lambda z: julia(z), [-2,2], [-2,2], points=800000, verbose=True)
