#!/usr/bin/python
from mpmath import *
import pylab

def r(z):
	return (z**21 -1)

def s(z):
	return (z**3 - 1)


def anewt(z):
	a = 0.0
	R = z
	S = z
	for u in range(1,100):
		M = r(R)
		N = s(S)
		a = a + M*N
		R = R - M/(21*R**20)
		S = S - N/(3*S**2)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-2,2], [-2,2], points=20000000, dpi=400, verbose=True, file="horned.png")