#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp


def wrap(z):
	return z/abs(z)

def g(z,q):
	return fp.nsum(lambda n: (q**(n**2))*(fp.cos(n*z)**2), [1,inf])

def h(z,q):
	return fp.nsum(lambda n: -(q**(n**2))*(fp.sin(n*z)**2), [1,inf])


Q = 0.9*fp.exp(2*pi*j/6)

fp.cplot(lambda z: wrap(g(z,Q)), [-10,10], [-10,10], points=100000, verbose=True, file="cossault.png")
fp.cplot(lambda z: wrap(h(z,Q)), [-10,10], [-10,10], points=100000, verbose=True, file="sinsault.png")
