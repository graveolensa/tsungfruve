#!/usr/bin/python
from mpmath import *
import pylab

for u in range(1,200):
	a = limit(lambda z: zeta(zetazero(u)+z)/z, 0)
	h = a/abs(a)
	print polar(h)