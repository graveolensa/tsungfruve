#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

'''
\sum_{n=1}^{\infty} \sum_{m=1}^{\infty} \frac{1-\cos(q^{nm})}{\cosh(1/q^{mn})}
'''

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: (1-fp.cos(q**(m*n)))/fp.qp(-q,q**(m**n)), [1,inf]), [1,inf])
		return A/abs(A)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="doblevida.png")
