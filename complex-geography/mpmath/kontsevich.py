#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def kontsevich(q):
		if(abs(q)>1.0):
			return 0.0
		else:
			return fp.nsum(lambda m: fp.qp(q,q,m), [0,inf])

fp.cplot(lambda z:kontsevich(z), [-1,1], [-1,1], points=100000, verbose=True, file="kont.png")