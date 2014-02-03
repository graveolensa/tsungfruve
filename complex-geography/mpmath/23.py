#!/usr/bin/python
from mpmath import *
import pylab

def W(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: fp.qp(-1,q*q,n)*((-1)**n)*(q**n)/fp.qp(q,q*q,n), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: W(q), [-1,1], [-1,1], points=100000, verbose=True, file="polydull.png")