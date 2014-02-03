#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def u(t):
	return (fp.sin(t)**2)/fp.cbrt(1+t**7)

def r(n):
	return fp.quad(lambda t: u(t), [0,n])

def a(z):
	if(abs(z)<1.0):
		return 0.0
	else:
		A = fp.nsum(lambda n: r(n)*(z**n), [0,inf])
		return A/abs(A)

fp.cplot(lambda z: a(z), [-1,1], [-1,1], points=100000, verbose=True, file="thenot.png")