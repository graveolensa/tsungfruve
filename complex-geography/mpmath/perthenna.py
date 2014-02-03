#!/usr/bin/python
from mpmath import *
import pylab

Q = 0.9*exp(pi*j/6.0)


def rel(z):
	u = fp.jtheta(3,z,Q)
	if(abs(u)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (u**n)/(1-u**n), [1,inf])
		return a/abs(a)


fp.cplot(lambda z: rel(z), [-8,8], [-8,8], points=10000000, dpi=400, verbose=True, file="chapmany.png")