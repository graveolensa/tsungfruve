#!/usr/bin/python
from mpmath import *
import pylab

r = fp.exp(2*pi*j/7.0)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nprod(lambda n: 1-r*fib(n)*(q**n), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=20000000, dpi=400, verbose=True, file="zzoiga.png1")