#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

c = 0.001
d = 0.95-0.31224*j

def f(z):
	return (z**3 + c)/(d*z)

def julia(z):
	for i in range(1,150):
		z = f(z)
	return z/abs(z)

fp.cplot(lambda z: julia(z), [-1.5, 1.5], [-1.5, 1.5], points=100000, verbose=True, file="ijon.png") 