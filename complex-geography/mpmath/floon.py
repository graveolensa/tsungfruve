#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	a = 0.0
	for u in range(1,100):
		a = a + ((z**3) - 1)**u
		z = z - (z**3 -1)/(3*z**2)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-2,2], [-2,2], points=20000000, dpi=400, verbose=True, file="artikulat.png")