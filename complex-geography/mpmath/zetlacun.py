#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A=fp.nsum(lambda n: fp.exp(j*fp.zeta(n)/(pi**(n-1)))*(q**n), [2,inf])
		return A/abs(A)
fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="zetlacun.png")