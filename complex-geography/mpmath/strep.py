#!/usr/bin/python
from mpmath import *
import pylab
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = 0
		for u in range(0,100):
			v = 2.0*u
			w = v + 1
			A = A + q**(v-q**(v+q**(v-q**v)))
			A = A * (1 - q**(w+q**(w-q**(w+q**w))))
		return A/abs(A)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="sqeeky2.png")