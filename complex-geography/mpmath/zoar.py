#!/usr/bin/python
from mpmath import *
import pylab

r = fp.exp(2.0*pi*j/7.0)

def anewt(z):
	a = 0.0
	for u in range(1,100):
		s = fp.exp(fp.cos(z**7))
		t = fp.exp(fp.sin(z**7))
		A = s/(1-t)
		a = a + (r**u)*A
		z = z - A/(( 7*(z**6) * s*(t-1)*fp.sin(z**7) + t*fp.cos(z**7))/((t-1)**2))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-4,4], [-4,4], points=20000000, dpi=400, verbose=True, file="zynthio.png")