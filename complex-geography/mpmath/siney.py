#!/usr/bin/python
from mpmath import *
import pylab

def siner(z):
	a = 0.0
	for u in range(1,200):
		z = fp.sin(z)
		a = a + ((-1)**u)*z
	return a/abs(a)

fp.cplot(lambda z: siner(z), [-10,10], [-10,10], points=10000000, dpi=400, verbose=True, file="bittererer.png")