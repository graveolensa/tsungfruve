#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

# def f(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		a = fp.nprod(lambda n: 1-(q**(n**3))*fp.qp(-q,q**(3**n)), [1,inf])
# 		return a/abs(a)

def A(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a=fp.nprod(lambda n: (1-(q**(2**n))*fp.qp(-q,q**(n**2)))/fp.qp(-q,q**(2**n)), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: A(q), [-1,1], [-1,1], points=100000, verbose=True, file="leftorama2.png")