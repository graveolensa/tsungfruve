#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


def r(z):
	if(abs(z)>1.0):
		return fp.jtheta(3,z,1/z)
	else:
		return fp.jtheta(3,z,z)

def newt(z):
	for n in range(1,10):
		z = z - r(z)/fp.diff(lambda u: r(u), z)
	return z/abs(z)

fp.cplot(lambda z: newt(z), [-2,2], [-2,2], points=100000, verbose=True, file='oddthop.png')