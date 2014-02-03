#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def g(q):
	if(abs(q)>1.5):
		return 0.0
	else:
		a = fp.nsum(lambda n: fp.exp(2*pi*j*n*fp.cos(n+q**n))*(q**(3**n)), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1.5,1.5], [-1.5,1.5], points=100000, verbose=True, file="euphrosyne2.png")