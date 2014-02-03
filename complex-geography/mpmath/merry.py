#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	r = z
	for o in range(1,100):
		r = r - (1-r**7)/(7*r**6)
	''' this gets us a seventh root of unity '''
	s = z
	a = 0.0
	for u in range(1,100):
		a = a + (r**u) * (1-s**7)
		s = s - (1-s**7)/(7*s**6)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-1.1, 1.1], [-1.1, 1.1], points=20000000, dpi=400, verbose=True, file="zoompth.png")