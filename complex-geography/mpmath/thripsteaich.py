#!/usr/bin/python
from mpmath import *
import pylab


'''
\prod_{a,b\in\mathbb{N}}\left[1-\frac{q^{ab}}{(1-q^{a})(1-q^{b})}\right]
too slow
'''

s
def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		r = fp.nprod(lambda a: fp.nprod(lambda b: 1-(q**(a*b))/((1-q**a)*(1-q**b)), [1,inf]), [1,inf])
		return r/abs(r)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="greenlemons.png")