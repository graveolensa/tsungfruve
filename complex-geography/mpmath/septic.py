#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


'''
Septic Theta functions, see
http://arxiv.org/pdf/1304.0694v1.pdf
'''



def a(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = - fp.nsum(lambda n: ((-1)**n)*(q**(((14*n+5)**2)/56)), [-inf,inf])
		return A/abs(A)


def b(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda n: ((-1)**n)*(q**(((14*n+3)**2)/56)), [-inf,inf])
		return A/abs(A)


def c(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A =  fp.nsum(lambda n: ((-1)**n)*(q**(((14*n+1)**2)/56)), [-inf,inf])
		return A/abs(A)



fp.cplot(lambda q: a(q), [-1,1], [-1,1], points=100000, verbose=True, file="septicaq.png")
fp.cplot(lambda q: b(q), [-1,1], [-1,1], points=100000, verbose=True, file="septicbq.png")
fp.cplot(lambda q: c(q), [-1,1], [-1,1], points=100000, verbose=True, file="septiccq.png")