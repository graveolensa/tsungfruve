#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	a = 0.0
	for u in range(1,100):
		a = a + fp.zeta(z)
		z = z - fp.zeta(z)/diff(lambda u: zeta(u), z)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-10,10], [-10,10], points=100000, verbose=True, file="akamawhat.png")