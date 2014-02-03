#!/usr/bin/python
from mpmath import *
import pylab

'''metarhizogenous function of a smoketrail lacunary'''

def L(q):
	return fp.nsum(lambda n: q**(n-(q**(n-q**(n-q**n)))), [1,inf])

def DL(q):
	return fp.nsum(lambda n: (q**(n-1 - (q**(n-q**n)) - (q**(n-q**(n-q**n)))))*( -n*((( q**n)*fp.log(q))**3) - ((q**n)-n)*((fp.log(q)*(q**n)**2)) + (fp.log(q)*(q**n))*(q**n - n*(q**(q**n))) + (n*q**(q**(n-q**n)) - q**n)*(q**(q**n))), [1,inf])


def anewt(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = 0.0
		for u in range(1,100):
			el = L(q)
			dl = DL(q)
			a = a + L
			q = q - el/dl
		return a/abs(a)

fp.cplot(lambda q: anewt(q), [-1,1], [-1,1], points=20000000, dpi=400, verbose=True, file="metasmoketrail.png"