#!/usr/bin/python
from mpmath import *
import pylab


def g(z):
	A = fp.nsum(lambda n: (1+1/n)**(z*n), [1,inf])
	return A/abs(A)

fp.cplot(lambda z: g(z), [-10,10], [-10,10], points=10000000, verbose=True, file="schala.png")