#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

# def g(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		a = fp.nprod(lambda n: 1+ acosh((q**n)*(1+asinh(q**n))), [1,inf])
# 		return a/abs(a)


# def g(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		a = fp.nsum(lambda n: acosh(1-q**n)/asinh(q**n), [1,inf])
# 		return a/abs(a)
# s


def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda m: fp.nsum(lambda n: fp.exp(2*pi*m*(1-q**(m*n))/n)*q**(m*n*(1-q**(m*n))), [1,inf]), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="kayapo.png")