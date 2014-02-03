#!/usr/bin/python
from mpmath import *
import pylab

def u(z):
	return fp.sin(z**7)

def anewt(z):
	a = 0.0
	for o in range(1,100):
		p = u(z)
		s = p**(p**p)
		a = a + s
		z = z - s/(7.0*(z**6)* (p**(p**p +p -1))*fp.cos(z**7)*(p*fp.log(p)*(1+fp.log(p))+1))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-3,3], [-3,3], points=20000000, verbose=True, dpi=400, file="bittered.png")