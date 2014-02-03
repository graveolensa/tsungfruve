#!/usr/bin/python
from mpmath import *
import pylab




def anewt(z):
	a = 0
	for u in range(0,100):
		a = a + fp.sin(fp.exp(z)) - fp.exp(fp.cos(z)) - z
		z = z - (fp.sin(fp.exp(z)) - fp.exp(fp.cos(z)) - z)/(fp.exp(z)*fp.cos(fp.exp(z)) + fp.sin(z)*fp.exp(fp.cos(z)) -1)
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-10,0], [-5,5], points=10000000, dpi=400, verbose=True, file="ahfka.png")
