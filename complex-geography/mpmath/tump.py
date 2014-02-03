#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp


# \sum_{n=1}^{\infty}\sum_{m=n}^{\infty}q^{m}(q;q^{n(1-q^{m})})_{\infty}

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		a = fp.nsum(lambda n: fp.nsum(lambda m: (q**m)*fp.qp(q,q**(n*(1-q**m))), [n,inf]), [1,inf])
		return a/abs(a)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="wormelow.png")