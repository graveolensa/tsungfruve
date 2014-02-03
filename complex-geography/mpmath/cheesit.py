#!/usr/bin/python
from mpmath import *
import pylab

r = 0.9*fp.exp(2*pi*j/7.0)

def anewt(z):
	a = 0.0
	for u in range(1,100):
		a = a + fp.sin(z* r**(u**2))
		z = z - fp.tan(z)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-3,3], [-3,3], points=20000000, dpi=400, verbose=True, file="arratna.png")