#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	a = 0.0
	for u in range(1,100):
		a = a + (fp.sin(z**7)/(fp.sin(z)**7))
		z = z - (fp.sin(z**7)/(fp.sin(z)**7))/(-7*fp.sin(z**7)*fp.cot(z)*(fp.csc(z)**7) + 7*(z**6)*(fp.cos(z)**7)*(fp.csc(z)**7))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-1,1], [-2,2], points=10000000, dpi=400, verbose=True, file="thiende.png")		