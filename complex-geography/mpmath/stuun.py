#!/usr/bin/python
from mpmath import * 
import pylab

def g(z):
	A=fp.nsum(lambda n: ((-z)**n)/(fp.fac(n)*fp.log(n)), [2,inf])
	return A/abs(A)
fp.cplot(lambda z: g(z), [-200,200], [-200,200], points=100000, verbose=True, file="arpoovian.png")