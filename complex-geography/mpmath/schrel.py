#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nprod(lambda m: fp.nprod(lambda n: fp.qp(-q,q**(m**n))*fp.qp(-q,q**(n**m)), [2,inf]), [2,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-0.01,0.01], [-0.01,0.01], points=200000, dpi=300, verbose=True, file="beringia2.png")