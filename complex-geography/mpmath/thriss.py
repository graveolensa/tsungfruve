#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

r = exp(2*pi*j/7.0)

def t(q,n):
	return fp.nprod(lambda m: 1-q**(m**n), [1,inf])

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: ((r*q)**n)/t(q,n), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="gherkins.png")