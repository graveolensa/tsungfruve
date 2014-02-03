#!/usr/bin/python
from mpmath import *
import pylab

def R(z):
	return fp.cosh(1-fp.sin(z))*fp.sinh(1-fp.cos(z))

def S(z):
	return fp.sin(z)*fp.cosh(1-fp.cos(z))*fp.cosh(1-fp.sin(z))-fp.cos(z)*fp.sinh(1-fp.sin(z))*fp.sinh(1-fp.cos(z))

def anewt(z):
	a = 0.0
	for u in range(1,100):
		r = R(z)
		s = S(z)
		a = a + r
		''' Newton-Raphson '''
		A = z - r/s
		''' Steffensen's '''
		B = z - r*r/(R(z+r)-r)
		z = fp.agm(A,B)	
	return a/abs/(a)

fp.cplot(lambda z: anewt(z), [-8.8], [-8,8], points=20000000, dpi=400, verbose=True, file="risottoi.png")
