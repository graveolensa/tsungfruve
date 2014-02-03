#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

def carlitz(z,theta,q):
	A = z+ fp.nsum(lambda n: (z**(q**n))/fp.nprod(lambda m: (theta**(q**m))-(theta**(q**(m-1))), [1,n-1]), [1,inf])
	return A/abs(A)


'''
here q is the power of a prime, choose 27
let theta be e^1 (we know that works)
'''

fp.cplot(lambda z: carlitz(z,e,27), [-20,20], [-20,20], points=1000000, verbose=True, file="carlitza.png")
