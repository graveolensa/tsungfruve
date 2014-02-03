#!/usr/bin/python
from mpmath import *
import pylab

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: fp.exp((2*pi+((-1)**(n+1))*(n**(1/n)))*j)*((-1)**(n+1))*(q**n), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, verbose=True, file="lyrallihot.png")