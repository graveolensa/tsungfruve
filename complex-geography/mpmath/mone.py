#!/usr/bin/python
from mpmath import *
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda m: fp.nsum(lambda n: q**(n-q**m), [1,inf]), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="pommeterre.png")