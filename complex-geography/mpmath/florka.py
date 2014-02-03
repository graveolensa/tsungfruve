#!/usr/bin/python
from mpmath import *
import pylab

def g(q):
	if(abs(q)>1.00):
		return 0.0
	else:
		a = fp.nsum(lambda m: fp.nsum(lambda n: (q**(m+n))/(1-q**(3*m+n)), [1,3*m*m]), [1,inf])
		return a/abs(a)

		
		

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="cornering.png")~