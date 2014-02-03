#!/usr/bin/python
from mpmath import *
import pylab

def s(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (q**(n**2))*(fp.sin( (n - q**(2**n - q**n) )/(n + q**(2**n + q**n) )  ) **2), [1,inf])
		return a/abs(a)


def c(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (q**(n**2))*(fp.cos( (n - q**(2**n - q**n) )/(n + q**(2**n + q**n) )  ) **2), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: s(q), [-1,1], [-1,1], points=20000000, verbose=True, dpi=400, file="sinjo.png")
fp.cplot(lambda q: s(q), [-1,1], [-1,1], points=20000000, verbose=True, dpi=400, file="cosjo.png")
