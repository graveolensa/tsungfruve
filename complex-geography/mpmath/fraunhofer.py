#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def g(z):
	A = fp.nsum(lambda n: fp.exp(j*re(z)*fp.cos(2*pi*n/5) + j*im(z)*fp.sin(2*pi*n/5)), [1,5])
	return A/abs(A)

fp.cplot(lambda z: g(z), [-100,100], [-100,100], points=10000000, dpi=400, verbose=True, file="frau.png")