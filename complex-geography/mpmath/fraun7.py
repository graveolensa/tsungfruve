#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def g(z):
	A = fp.nsum(lambda n: fp.exp(j*re(z)*fp.cos(2*pi*n/7) + j*im(z)*fp.sin(2*pi*n/7)), [1,7])
	return A/abs(A)

fp.cplot(lambda z: g(z), [-100,100], [-100,100], points=100000, verbose=True, file="frau.png")