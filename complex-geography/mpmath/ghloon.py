#!/usr/bin/python
from mpmath import *
import pylab

g = 0.10291 + 0.11295*j
c = j
def ror(z):
	zer = g
	for u in range(1,100):
		zer = zer**z + c
	return zer/abs(zer)


fp.cplot(lambda z: ror(z), [30,30], [30,30], points=20000000, dpi=400, verbose=True, file="arbeit.png")