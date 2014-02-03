#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

r = exp(2*pi*j/7)
u = exp(2*pi*j/3)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (r**n)*(q**(n**2))/fp.qp(-q,(q**n)*(u**(n**2))), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, verbose=True, dpi=400, file="andorin.png")