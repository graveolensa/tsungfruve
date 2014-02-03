#!/usr/bin/python
from mpmath import *
import pylab
import mpmath.libmp

def rogers(q):
	if(abs(q)>=1.0):
		return 0.0
	else:
		return (q**1/5.0)*fp.qp(q,q**5)*qp(q**4,q**5)/(qp(q**2,q**5)*qp(q**3,q**5))

def many(q):
	s = q
	for a in range(1,60):
		S = rogers(s)
		s = S
	return s

fp.cplot(lambda q: many(q), [-1,1], [-1,1], points=200000, verbose=True, file="rogersram.png")