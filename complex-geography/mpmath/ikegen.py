#!/usr/bin/python
from mpmath import *
import pylab

s = sqrt(3)/2.0
v = 1/2.0



def jules(z):
	for a in range(1,30):
		z = (z-s)*(z+s)*(z-v)*(z+v)
	return z/abs(z)

fp.cplot(lambda z: jules(z), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="ikebday.png")