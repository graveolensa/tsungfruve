#!/usr/bin/python

from mpmath import *
import pylab

def g(q):
		if(abs(q)>1.0):
			return 0.0
		else:
			return fp.nprod(lambda n: (1-q**n)**(n**2.0), [1,inf])


fp.cplot(lambda q: g(q), [-1,1], [-1,1], verbose=True, points=200000, file="augustina.png")