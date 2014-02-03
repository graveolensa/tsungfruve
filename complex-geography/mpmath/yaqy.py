#!/usr/bin/python
from mpmath import *
import pylab

'''
Here the Newton-Raphsoning is on sin(1-e^cos(z)), in order
for that to be zero, 1-e^(cos(z)) has to be zero or a multiple of such.

in order for that to be the case, cos(z) must equal 0. 

'''


def anewt(z):
	a = 1.0
	for u in range(1,100):
		a = a * (1 - fp.cos(z**u))
		z = z - fp.tan(1-fp.exp(fp.cos(z)))*fp.csc(z)*fp.exp(-fp.cos(z))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-4,4], [-4,4], points=20000000, dpi=400, verbose=True, file="zuzfoon.png")