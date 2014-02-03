#!/usr/bin/python
from mpmath import *
import pylab

def g(z):
	return fp.zeta(z)

def anewt(z):
	A = 0.0 
	for u in range(1,100):
		A = A + fp.zeta(z)
		z = z - fp.zeta(z)/zeta(z,1,1)
	return A/abs(A)

fp.cplot(lambda z: anewt(z), [-30, 30], [-30, 30], verbose=True, points=10000000, dpi=400, file="drosophobia.png")