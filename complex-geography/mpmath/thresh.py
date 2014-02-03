#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

'''
\sum_{m=1}^{\infty}\sum_{n=1}^{\infty} \frac{q^{m}-q^{n}}{1+q^{m}+q^{n}}
'''

def G(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: (q**(m*n))/(1+(q**m)-(q**n)), [1,inf]), [1,inf])
		return A/abs(A)

fp.cplot(lambda q: G(q), [-1,1], [-1,1], points=100000, verbose=True, file="strack.png")
