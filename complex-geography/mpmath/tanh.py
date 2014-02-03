#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


def T3(z):
	return 2*(fp.cosh(2*z)-2)*(fp.sech(z)**4)

def T2(z):
	return -2*fp.tanh(z)*(fp.sech(z)**2)

def T1(z):
	return fp.sech(z)**2

def schwarzian(z):
	return (T3(z)/T1(z) - (3/2.0)*((T2(z)/T1(z))**2.0))

def newt(z):
	for u in range(1,30):
		z = z - fp.tanh(z)/schwarzian(z)
	return z/abs(z)

fp.cplot(lambda z: newt(z), [-10,10], [-10,10], points=100000, verbose=True, file="tanhschwarznewton.png")