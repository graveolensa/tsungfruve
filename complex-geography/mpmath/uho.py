#!/usr/bin/python
from mpmath import *
import pylab


def anewt(z):
	''' set the accumulant to zero '''
	a = 0.0
	for u in range(1,30):
		a = a + 1.0+fp.nsum(lambda n: (z/n)**n, [1,inf])
		z = z - (1.0+fp.nsum(lambda n: (z/n)**n, [1,inf]))/fp.nsum(lambda n: (z/n)**(n-1), [1,inf])
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-8,8], [-8,8], points=10000000, dpi=400, verbose=True, file="crailin.png")