#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

# def g(q):
# 	if (abs(q)>1.0):
# 		return 0.0
# 	else:
# 		v = 0.0
# 		for n in range(1,60):
# 			u = 2*n-1
# 			v = v + ((-1)**u)*(q**(u**3))*fp.qp(-q,q**(2*u)) 
# 			w = 2*n
# 			v = v * (1-q**(3*w))*fp.qp(-q*q,q**w)
# 		return v/abs(v)

# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=200000, verbose=True, file="altrude.png")

# def g(q):
# 	if (abs(q)>1.0):
# 		return 0.0
# 	else:
# 		v = 0.0
# 		for n in range(1,100):
# 			u = 2*n-1
# 			v = v + q**(3**u)
# 			w = 2*n
# 			v = v * (1-q**(3**w))
# 		return v/abs(v)

# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=200000, verbose=True, file="toledo.png")

def g(q):
	if (abs(q)>1.0):
		return 0.0
	else:
		v = 0.0
		for n in range(1,100):
			u = 2*n-1
			v = v + fp.qp(-q,q**u)*(q**(3**u))
			w = 2*n
			v = v * (1-q**(3**w))/fp.qp(q,q**w)
		return v/abs(v)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=200000, verbose=True, file="cleveland.png")