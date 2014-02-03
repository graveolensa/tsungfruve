#!/usr/bin/python
from mpmath import *
import pylab


def g(z):
	a = fp.nsum(lambda n: fp.sin(z)*( 1/fac(4*n) - 1/fac(4*n+2) ) + fp.cos(z)*(1/fac(4*n+1)-1/fac(4*n+3)), [1,inf])
	return a/abs(a)


fp.cplot(lambda z: g(z), [-10,10], [-10,10], points=100000, verbose=True, file="ascorbica.png")