#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

a = cbrt(7)

def newt(z):
	for u in range(1,30):
		z = z - fp.polylog(a,z)/fp.diff(lambda r: fp.polylog(a,r), z)	
	return z/abs(z)



fp.cplot(lambda z: newt(z), [-5,5], [-5,5], points=100000, verbose=True, file="polylog.png")