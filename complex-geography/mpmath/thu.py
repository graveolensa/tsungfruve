#!/usr/bin/python
from mpmath import *
import pylab

def g(q):
	if(abs(q)>=1.0):
		return 0.0
	else:
		A=fp.nsum(lambda m: fp.nsum(lambda n: fp.exp(2*pi*j*m/n)*(q**(m**n)), [1,inf]), [2,inf])
		return A/abs(A)

		
fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=200000, verbose=True, file="eland.png")