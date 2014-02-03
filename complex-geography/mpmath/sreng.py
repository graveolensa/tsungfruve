#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


def Y(q,p):
	if (abs(q)>1.0)|(abs(p)>1.0):
		return 0.0
	else:
		R = fp.nsum(lambda n: (q**(n**2))*(p**(n**4)), [-inf,inf])
		return R/abs(R)

P = 0.37*exp(pi*j/7)

fp.cplot(lambda q: Y(q,P), [-1,1], [-1,1], points=100000, verbose=True, file="forded.png")
