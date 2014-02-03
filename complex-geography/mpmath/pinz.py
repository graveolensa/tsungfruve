#!/usr/bin/python
from mpmath import *
import pylab

def anewt(z):
	r = z
	s = z
	a =  0.0
	for u in range(1,100):
		R = r - fp.tan(fp.sin(r)-s)
		S = s + fp.cos(fp.tan(s)+r)
		r = R
		s = S
		'''
		so we don't have f' and f, and
		integrating to find them in the above
		case is somewhat nontrivial. so let's just 
		try something and see what effect it has
		'''
		a = a + fp.cosh(r-fp.sin(s))-fp.sinh(s+fp.cos(r))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-3,3], [-3,3], points=20000000, verbose=True, dpi=400, file="wildgreen.png")