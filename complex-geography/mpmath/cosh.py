#!/usr/bin/python

from mpmath import *
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A= fp.nprod(lambda n: fp.cosh(q**n), [1,inf])
		return A/abs(A)

def f(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A= fp.nprod(lambda n: fp.cos(q**n), [1,inf])
		return A/abs(A)

def r(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A= fp.nsum(lambda n: fp.sinh(q**n), [1,inf])
		return A/abs(A)

def s(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A= fp.nsum(lambda n: fp.sin(q**n), [1,inf])
		return A/abs(A)


fp.cplot(lambda q:g(q), [-1,1], [-1,1], points=100000, verbose=True, file="coshprod.png")
fp.cplot(lambda q:f(q), [-1,1], [-1,1], points=100000, verbose=True, file="cosprod.png")
fp.cplot(lambda q:r(q), [-1,1], [-1,1], points=100000, verbose=True, file="sinhsum.png")
fp.cplot(lambda q:s(q), [-1,1], [-1,1], points=100000, verbose=True, file="sinsum.png")