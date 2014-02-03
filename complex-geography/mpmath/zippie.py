#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nprod(lambda m: 1-(q**m)*fp.nprod(lambda n: 1-fp.exp(2*pi*j*m/n)*(q**(m*n)), [1,inf]), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="sanvalvwag.png")