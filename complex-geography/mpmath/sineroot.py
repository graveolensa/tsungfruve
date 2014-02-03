#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def newt(z):
	for u in range(1,200):
		z = z - (fp.cos(fp.exp(z))-fp.exp(fp.cos(z)) - z)/(-fp.exp(z)*fp.sin(fp.exp(z))+fp.sin(z)*fp.exp(fp.cos(z))-1.0)
	return z/abs(z)

fp.cplot(lambda z: newt(z), [-14,1], [-4,4], points=800000, dpi=300, verbose=True, file="finer.png")		