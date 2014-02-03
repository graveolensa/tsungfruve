#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

'''
Mock Modular Forms / Mock Theta Functions
See http://http://en.wikipedia.org/wiki/Mock_theta_function
'''

'''
Order 2
'''

def A(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**((n+1)**2))*fp.qp(-q,q**2,n)/(fp.qp(q,q**2,n+1)**2), [0,inf])
		return out/abs(out)

def B(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**((n+1)*n))*fp.qp(-q*q,q**2,n)/(fp.qp(q,q**2,n+1)**2), [0,inf])
		return out/abs(out)

def mu(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: ((-1)**n)*(q**(n*n))*fp.qp(q,q**2,n)/(fp.qp(-q**2,q**2,n)**2), [0,inf])
		return out/abs(out)

fp.cplot(lambda q: A(q), [-1,1], [-1,1], points=100000, verbose=True, file="mock.theta.Aq.png")
fp.cplot(lambda q: B(q), [-1,1], [-1,1], points=100000, verbose=True, file="mock.theta.Bq.png")
fp.cplot(lambda q: mu(q), [-1,1], [-1,1], points=100000, verbose=True, file="mock.theta.muq.png")