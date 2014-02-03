#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: jtheta(3,-q,q**(2*n))*jtheta(3,q,-q**(3*n))*(q**n)/jtheta(3,q,q**(7*n)), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="driplet.png")