#!/usr/bin/python
from mpmath import *
import pylab

def g(z):
	if(abs(z)>=1.0):
		return 0.0
	else:
		A = fp.nprod(lambda n: 1 + (z**n)/(1-z**n), [1,inf])
		s = A/abs(A)
		return s

fp.cplot(lambda z: g(z), [-1,1], [-1,1], points=200000, verbose=True, file="cassegrain.png")