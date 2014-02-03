#!/usr/bin/python
from mpmath import *
import pylab

w = fp.exp(2.0*pi*j/7.0)
def h(n):
	return floor(fp.gamma(cbrt(n)+2**(-1/7.0)))

def g(q):
	if(abs(q)>=1.0):
		return 0.0
	else:
		return fp.nsum(lambda n: (w**h(n))*(q**(n**2.0)), [-inf, inf])

fp.cplot(lambda z: g(z), [-1,1], [-1,1], points=200000, verbose=True, file="eyre.png")