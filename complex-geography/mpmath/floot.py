#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	a = 0.0
	for u in range(1,100):
		a = a + (fp.sinh(z)**fp.cos(z) - fp.cosh(z)**fp.sin(z))
		z = z - ((fp.sinh(z)**fp.cos(z) - fp.cosh(z)**fp.sin(z)))/((fp.sinh(z)**fp.cos(z))*(fp.cos(z)*fp.coth(z)-fp.sin(z)*fp.log(fp.sinh(z))) - (fp.cosh(z)**fp.sin(z))*(fp.sin(z)*fp.tanh(z)+fp.cos(z)*fp.log(fp.cosh(z))))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-8,8], [-8,8], points=20000000, dpi=400, verbose=True, file="abjectia.png")