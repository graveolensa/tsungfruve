#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda m: fp.nsum(lambda n: (m**(3-q**n))*(n**(3+q**m))*(q**(m+n)), [1,inf]), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="dischord.png")