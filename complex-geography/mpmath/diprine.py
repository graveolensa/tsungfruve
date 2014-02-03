#!/usr/bin/python
from mpmath import *
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = 0.0
		for n in range(1,100):
			v = 2*n - 1
			a = a + q**(n-q**(n+q**n))
			w = 2*n
			a = a * (1 - q**(n+q**(n-q**n)))
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, verbose=True, file="gilmerist.png") 