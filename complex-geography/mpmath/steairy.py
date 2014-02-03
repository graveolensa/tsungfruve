#!/usr/bin/python
from mpmath import *
import mpmath.libmp




def newt(z):
	for u in range(1,60):
		z = z - (fp.airyai(z)**2)/(fp.airyai(z + fp.airyai(z))-fp.airyai(z))
	return z/abs(z)

fp.cplot(lambda z: newt(z), [-20,20], [-20,20], points=10000000, dpi=400 ,verbose=True, file="stefairy.png")