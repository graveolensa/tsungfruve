#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab




r = exp(2*pi*j/7)


def G(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nprod(lambda n: 1 - ((r**(3**n))*(q**(7**n)))*fp.qp(-q,(r**(n**3))*(q**(n**2))), [1,inf])
		return A/abs(A)

fp.cplot(lambda q: G(q), [-1,1], [-1,1], points=100000, dpi=400, verbose=True, file="ibex2.png")