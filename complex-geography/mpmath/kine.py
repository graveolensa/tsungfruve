#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (q**(fp.cosh(q**n)*(n**3)))*fp.qp(-q,q**(fp.cos(q**n)*(3**n))), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="nepetalactone.png")