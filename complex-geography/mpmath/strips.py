#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


def g(z):
	b=floor(z)
	u=ceil(z)
	r = z+100*b*j-b
	A = zeta(r)
	return A/abs(A)
	

fp.cplot(lambda z: g(z), [0,100], [0,100], points=1000000,  verbose=True, file="zrips2.png")