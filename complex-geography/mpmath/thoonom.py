#!/usr/bin/python
from mpmath import *
import pylab

def u(z):
	return fp.sin(z**2-fp.cos(z**3+fp.sin(z**5)))

def anewt(z):
	a = 0.0
	for o in range(1,100):
		U = u(z)
		a = a + U
		z = z - U/(z*fp.cos(z**2-fp.cos(z**3+fp.sin(z**5)))*(z*fp.sin(fp.sin(z**5)+z**3)*(5*z*z*fp.cos(z**5)+3)+2))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-4,4], [-4,4], points=20000000, verbose=True, dpi=400, file="gurusai.png")