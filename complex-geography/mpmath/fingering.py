#!/usr/bin/python
from mpmath import *
import pylab

def gruff(z):
	u = fp.zeta(z)
	if(arg(u)==0.0):
		out = 1.0
	else:
		out = 0.0
	return out

fp.cplot(lambda z: gruff(z), [-80,80], [-80,80], points=20000000, dpi=400, verbose=True, file="phalanges.png")
