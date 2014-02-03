#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

a = exp(2*pi*j/7)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: (q**(m**(7*n)))*(a**(m/n))/(fp.qp(q,-q**(7*n))*fp.qp(-q,q**(7*n))), [1,inf]), [2,inf])
		return A/abs(A)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="june1.2013.png")