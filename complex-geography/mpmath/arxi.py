#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

def O(z):
	return (z**5)*(2+z)*(2+2*z+z*z)/((1+2*z)*(1+2*z+2*z*z))

def jules(z):
	for i in range(1,200):
		z = O(z)
	return z/abs(z)

fp.cplot(lambda z: jules(z), [-50,80],[-65,65], points=100000, verbose=True, file="moranis.png")