#!/usr/bin/python
from mpmath import *
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: fp.exp(2*pi*j/n)*fp.zeta(n+q**n)*(q**n), [2,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=20000000, dpi=400, verbose=True, file="xhloope.png")