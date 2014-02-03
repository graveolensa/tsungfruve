#!/usr/bin/python
from mpmath import *
import pylab

''' metarhizogenous function on the unit disk of 
\sum_{n=1}^{\infty} \frac{q^{n^{3}}}{1+nq^{n}-\sqrt[3]{n}q^{2^{n}}}

Yeah this one is going to take a while to render

'''

def L(q):
	return fp.nsum(lambda n: (q**(n**3))/(1+n*(q**n)-cbrt(n)*(q**(2**n))), [1,inf])


def DL(q):
	return fp.nsum(lambda n: ((q**(n**3 -1))*(((2**n-n**3)*cbrt(n)*(q**(2**n)))+(n**2)*(-n**2 * q**n + q**n + n)))/((cbrt(n)*(q**(2**n))+n*(q**n) -1)**2), [1,inf])

def anewt(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = 0.0
		for u in range(1,100):
			'''
			this just saves us from having to recalculate L(q) more than once
			'''
			r = L(q)
			a = a + r
			''' Newton-Raphson method step '''
			q = q - r/DL(q)
		return a/abs(a)

fp.cplot(lambda q: anewt(q), [-1,1], [-1,1], points=20000000, dpi=400, verbose=True, file="schroneia.png")