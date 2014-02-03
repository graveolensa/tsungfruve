#!/usr/bin/python
from mpmath import *
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (q**n)*( (4.0/(8.0*n+1)) - (2.0/(8.0*n+4)) - (1.0/(8.0*n+5)) - (1/(8.0*n+6))), [0,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="bbp.png")