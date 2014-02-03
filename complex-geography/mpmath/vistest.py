#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def b(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return (fp.qp(q,q)**3)/fp.qp(q**3,q**3)

fp.cplot(lambda q: b(q), [-1,1], [-1,1], points=100000, verbose=True, file="bqtest.png")