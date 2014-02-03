#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def g(z):
	A=fp.nsum(lambda n: fp.exp(2.0*j*pi*(3**n)/(n**7)) * (z**n)/agm(3**n,7**n), [1,inf])
	return A/abs(A)

fp.cplot(lambda z: g(z), [-10,10], [-10,10], points=200000, verbose=True, file="inman.png")