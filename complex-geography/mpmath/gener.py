#!/usr/bin/python
from mpmath import *
import mpmath.libmp

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		s = 0
		for u in range(1,100):
			v = jtheta(3,q,q**u)
			s = s + (1-v)**((1-v)**(1-v))
		return s/abs(s)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="shrell.png")
