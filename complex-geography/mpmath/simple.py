#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	r = z
	s = z
	a = 0.0
	for u in range(1,100):
		p = s**3 - 1.0
		a = a + (r**(3-p)) - (r**(2-p)) + r**(1-p) -1.0
		r = r - (r**3 - r**2 + r -1.0)/(3*r**2 - 2**r + 1.0)
		s = s - p/(3*s**2)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-3,3], [-3,3], points=20000000, dpi=400, verbose=True, file="lienzoohte.png")