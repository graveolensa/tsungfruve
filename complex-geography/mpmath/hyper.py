#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	a = 0.0
	for u in range(0,100):
		a = a + (  fp.cosh(fp.sin(z)) -  fp.sinh(fp.cos(z))) - z
		z = z - (fp.cosh(fp.sin(z))-fp.sinh(fp.cos(z)) -z ) / (fp.cos(z) * fp.sinh(fp.sin(z)) +fp.sin(z) *fp.cosh(fp.cos(z)) - 1.0)
	return z/abs(z)

fp.cplot(lambda z: anewt(z), [-8,8], [-8,8], points=10000000, dpi=400, verbose=True, file="hyperify.png")
