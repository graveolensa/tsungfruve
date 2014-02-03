#!/usr/bin/python
from mpmath import *
import pylab

r = fp.exp(pi*j/12)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nprod(lambda n: (1-q**n)**(r**n), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=20000000, verbose=True, dpi=400, file="komil.png")