#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	a = 0.0
	for u in range(1,100):
		a = a + fp.tan(fp.tan(fp.tan(z))) - z
		z = z - (fp.tan(fp.tan(fp.tan(z))) - z)/( (fp.sec(z)**2)*(fp.sec(fp.tan(z))**2)*(fp.sec(fp.tan(fp.tan(z)))**2) -1.0)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-4*pi,4*pi], [-5,5], points=100000, verbose=True, file="oswaldo.png")