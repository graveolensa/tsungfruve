#!/usr/bin/python

from mpmath import *
import pylab

def g(z,q,a,b,c):
	if(abs(q)>1.0):
		return 0.0
	else:
		r = fp.nsum(lambda n: (q**(a*n*n+b*n+c))*fp.exp(2*n*j*z), [-inf,inf])
		return r/abs(r)

Q = 0.9*exp(pi*j/6)

fp.cplot(lambda z: g(z,Q,3,2,1), [-10,10], [-10,10], points=100000, verbose=True, file="sleepyng.png")
