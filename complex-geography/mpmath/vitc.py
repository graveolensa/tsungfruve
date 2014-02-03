#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nprod(lambda n: (1+q**(n*(1-q**(3*n+1))))/(1-q**(n*(1+q**(3*n+1)))), [1,inf])
		return A/abs(A)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="ascorbicide.png")