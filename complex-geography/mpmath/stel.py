#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


r = exp(2*pi*j/7)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (r**n)*(q**((3**n)*qp(-q,q**(7*n)))), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000,  verbose=True, file="bragma2.png")