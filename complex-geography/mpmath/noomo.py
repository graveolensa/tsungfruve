#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

def b(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return (fp.qp(q,q)**3)/fp.qp(q**3,q**3)

def c(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return 3*(q**(1/3.))*(fp.qp(q**3,q**3)**3)/fp.qp(q,q)

''' a(q) is going to be painful to write, but will be much faster
to evaluate in terms of qp than the infinite sum '''

def a(q):
	if(abs(q)> 1.0):
		return 0.0
	else:
		hack = ( fp.qp(-q,q**2)**2 )*fp.qp(q**2,q**2)*(fp.qp(-q**3,q**6)**2)*fp.qp(q**6,q**6)
		slash = 4.0*q* fp.qp(q**4,q**4)*fp.qp(q**12,q**12)/(fp.qp(q**2,q**4)*fp.qp(q**6,q**12))
		return hack+slash

def anewt(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		s = 0.0
		for u in range(1,100:)
		A = a(q)
		B = b(q)
		C = c(q)
		s = s + A
		'''
		the idea here is that the denominator is the derivative of the numerator
		with respect to B'''

		q = q - (A*B*B - C * fp.cos(B) + B*C*C)/(A*B/2.0 + C * fp.sin(B) + C*C)
	return s/abs(s)


fp.cplot(lambda q: anewt(q), [-1,1], [-1,1], points=20000000, dpi=400, verbose=True, file="borwat.png")