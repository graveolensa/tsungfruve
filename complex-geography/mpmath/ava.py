#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = nsum(lambda m: nsum(lambda n: ((m+q**(n*(1-q**m)))/(n+q**(m*(1-q**n))))*(q**(m+n)), [1,inf]), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="bulbasaur2.png")