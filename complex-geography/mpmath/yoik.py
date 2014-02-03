#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	r = z
	s = z
	a = 0.0
	for u in range(1,100):

		'''
		the idea here is that as u gets large, s will go to a root
		of sin(s) via Newton-Raphson, and r will go to a root
		of r^3 -r^2 +1 via Newton-Raphson
		'''
		a = a + ((r**(3-fp.sin(s))) - (r**(2-fp.sin(s))) + 1)
		r = r - (r**3 - r**2 + 1)/(3*r**2 - 2*r)
		s = s - fp.tan(s)
	return a/abs(a)

fp.cplot(lambda z:  anewt(z), [-4,4], [-4,4], points=20000000, dpi=400, verbose=True, file="sulita.png")