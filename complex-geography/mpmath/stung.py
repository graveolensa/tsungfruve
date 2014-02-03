#!/usr/bin/python
from mpmath import *
import pylab

w = fp.exp(2.0 * pi * j / 7.0)

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		return fp.nprod(lambda n: (1-(w**n)*(q**(7**n)))/(1-(q**(7**n))), [1,inf])

# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=200000, verbose=True, file="rubric.png")

# saved in rubric.png, unsurprisingly has seven-sided symmetry, not immediately visually 
# interesting


def a(q):
	if(abs(q)>=1.0):
		return 0.0
	else:
		return fp.nsum(lambda n: (w**(4*n*n+11*n+4))*(q**(n**3)), [1,inf])

fp.cplot(lambda q: a(q), [-1,1], [-1,1], points=200000, verbose=True, file="fibril.png")