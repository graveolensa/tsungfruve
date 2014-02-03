#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def newt(z):
	for u in range(0,100):
		z = z - (fp.exp(j*z)-j)/(j*fp.exp(j*z))
	return z

fp.cplot(lambda z: newt(z), [-15,15], [-15,15], points=800000, dpi=400,  verbose=True, file="cleese.png")