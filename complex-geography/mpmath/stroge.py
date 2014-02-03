#!/usr/bin/python

from mpmath import *
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda m: 1-fp.nprod(lambda n :(1-q**(m*n)), [1,inf])**(1/m), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="karkatvantas.png")
