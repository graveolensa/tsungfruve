#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nprod(lambda n: fp.cosh((q**n)*fp.qp(-q,q**(3*n)))/(1-q**(2**n)), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="msnerd.png")