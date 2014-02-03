#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

# def g(q):
# 	return fp.qp(q,q)

# u=exp(2*pi*j/7)

# def g(q):
# 	return fp.nsum(lambda n: (u**n)*q**(7**n), [0,inf])

def g(q):
	return jtheta(3,q,q)

def jackson(q):
	return (g(q*q)-g(q))/(q*q-q)

def newt(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		for r in range(1,30):
			if(abs(q)<1.0):
				q = q - g(q)/jackson(q)
		return q/abs(q)

fp.cplot(lambda q: newt(q), [-1,1], [-1,1], points=100000, verbose=True, file="jackson3.png")