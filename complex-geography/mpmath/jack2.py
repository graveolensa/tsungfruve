#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

# def g(q):
# 	return fp.qp(q,q)

# u=exp(2*pi*j/7)

# def g(q):
# 	return fp.nsum(lambda n: (u**n)*q**(7**n), [0,inf])

# def g(q):
# 	return fp.nprod(lambda n: 1-q**(n**2)-2*(q**(2**n)), [1,inf])

# def g(q):
# 	return q*fp.exp(j*arg(fp.kleinj(qbar=q)))

# def jackson(q):
# 	return (g(q*q)-g(q))/(q*q-q)

# def newt(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		for r in range(1,100):
# 			if(abs(q)<1.0):
# 				q = q - g(q)/jackson(q)
# 		return q/abs(q)

# fp.cplot(lambda q: newt(q), [-1,1], [-1,1], points=1000000, dpi=600, verbose=True, file="qkleinj2.png")

def g(q):
	return fp.lambertw(q)

def jackson(q):
	return (g(q*q)-g(q))/(q*q-q)

def newt(q):
	for r in range(1,100):
		if(abs(q)<1.0):
			q = q - g(q)/jackson(q)
	return q/abs(q)

fp.cplot(lambda q: newt(q), [-1,1], [-1,1], points=1000000, dpi=600, verbose=True, file="lambertw.png")