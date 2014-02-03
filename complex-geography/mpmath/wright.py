#!/usr/bin/python
from mpmath import *
import pylab

def wright(rho, beta, z):
	A=fp.nsum(lambda n: (z**n)/(fp.fac(n)*fp.gamma(rho*n+beta)), [0,inf)]	return A/abs(A)

R = 7.0**(1/3.0)
b  = 3*j+0.2110204

fp.cplot(lambda z: wright(R,b,z), [-2000,2000], [-2000,2000], points=200000, verbose=True, file="wright.png")