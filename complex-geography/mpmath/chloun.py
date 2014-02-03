#!/usr/bin/python
from mpmath import *
import pylab

r = fp.exp(2*pi*j/7.0)


'''
this is a metarhizogeous function which shares a factor, and I'll think of a better name
for it later
'''

def anewt(z):
	a = 0.0
	for u in range(1,100):
		h = 1 - fp.sin(z)**7
		a = a + (r**u)*h*(1-fp.exp(fp.cosh(z)))
		z = z + h/(7.0*fp.cos(z)* (fp.sin(z)**6))
	return a/abs(a)


fp.cplot(lambda z: anewt(z), [-3,3], [-3,3], points=20000000, dpi=400, verbose=True, file="soiechthe.png")
