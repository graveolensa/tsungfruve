#!/usr/bin/python
from mpmath import *
import pylab

def g(z):
	a = fp.nsum(lambda n: fp.exp((1/z)**n)/(n**3), [1,inf])
	return a/abs(a)

fp.cplot(lambda z: g(z), [-4,4], [-4,4], points=10000000, dpi=400, verbose=True, file="stentuka.png")