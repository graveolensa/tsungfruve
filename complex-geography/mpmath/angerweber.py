#!/usr/bin/python
from mpmath import *
import pylab

# define S1(nu,z):
def S1(nu,z):
	return fp.nsum(lambda k: ((-1)**k)*((z/2.0)**(2*k))/((fp.gamma(k+nu/2.0+1))*(k-nu/2.0+1.0)), [0,inf])

def S2(nu,z):
	return fp.nsum(lambda k: ((-1)**k)*((z/2.0)**(2*k+1))/((fp.gamma(k+nu/2.0+3/2.0))*(k-nu/2.0+3/2.0)), [0,inf])

# Anger Function
def J(nu,z):
	return fp.cos(pi*nu/2.0)*S1(nu,z) + fp.sin(pi*nu/2.0)*S2(nu,z)

# Weber Function
def E(nu,z):
	return fp.sin(pi*nu/2.0)*S1(nu,z) - fp.cos(pi*nu/2.0)*S2(nu,z)


def ghoo(z):
	x = re(z)
	y = im(z)
	v = J(x,y) + j*E(x,y)
	return v/abs(v)

fp.cplot(lambda z: ghoo(z), [-20,20], [-20,20], points=100000, verbose=True, file="weberanger.py")
