#!/usr/bin/python
from mpmath import *
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = 0.0
		for u in range(0,100):
			a = 3*u
			b = 3*u + 1
			c = 3*u + 2
			A = A + q**((a**3)-q**a)
			A = A * (1 - q**((3**(b-(q**b)))))
			A = A * fp.qp(q,q**(3*c))/(1-q**(c**3))
		return A/abs(A)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="duvitski.png")

