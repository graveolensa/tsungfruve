#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


r = exp(2*pi*j/7)

# def g(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		a = fp.nprod(lambda n: 1-(r**n)*(q**(n**7))/fp.qp(-q,q**(7**n)), [1,inf])
# 		return a/abs(a)

# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="batty2.png")


# def g(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		a = fp.nprod(lambda n: 1-q**(7**(n+q**n)), [1,inf])
# 		return a/abs(a)

# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="banbv.png")


r = exp(2*pi*j/7)
s = exp(2*pi*j/3)
t = exp(2*pi*j/21)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: (r**n)*(q**(3**n)), [1,inf])
		b = fp.nsum(lambda n: (s**n)*(q**(7**n)), [1,inf])
		c = fp.nsum(lambda n: (t**n)*(q**(21**n)), [1,inf])
		R = a*b/c
		return R/abs(R)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="flere.png")