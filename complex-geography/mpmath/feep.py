#!/usr/bin/python
from mpmath import *
import pylab

def g(q):
	if(abs(q)>=1.0):
		return 0.0
	else:
		A = fp.nsum(lambda n:  ((q**(3**n)) - (q**(n**3)))/(1.0-q**(3**n)), [1,inf])
		return A/abs(A)


fp.cplot(lambda z: g(z), [-1,1], [-1,1], points=200000, verbose=True, file="refractor.png")