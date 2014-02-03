#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

Z = sqrt((5-sqrt(5))/8)

a = 1/2.0
b = 1/2.0
c = 3/2.0

def poq(q,A,n):
	return fp.qp(q**(A-n+1),q)/fp.qp(q**(A+1),n)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		S = Z*fp.nsum(lambda n: poq(q,a,n)*poq(q,b,n)*(1-q**n)*(Z**(2*n))/poq(q,c,n), [1,inf])
		return S/abs(S)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=300, verbose=True, file="gaussy.png")