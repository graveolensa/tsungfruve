#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

'''
quintic theta functions. 
See Tim Huber's paper:
http://arxiv.org/pdf/1304.0684v1.pdf
/A Theory of Theta Functions to a Quintic Base/
'''


'''
Order 7 mock theta functions, See

# fp.cplot(lambda q: D(q), [-1,1], [-1,1], points=100000, verbose=True, file="quinticDq.png")
http://en.wikipedia.org/wiki/Mock_theta_function
'''

def F0(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return fp.nsum(lambda n: (q**(n**2))/fp.qp(q**(n+1),q,n), [0,inf])


def F1(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return fp.nsum(lambda n: (q**(n**2))/fp.qp(q**n,q,n), [0,inf])

def F2(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return fp.nsum(lambda n: (q**(n*(n+1)))/fp.qp(q**(n+1),q,n+1), [0,inf])


fp.cplot(lambda q: F0(q), [-1,1], [-1,1], points=100000, verbose=True, file="theta.mock.7.F0.png")
fp.cplot(lambda q: F1(q), [-1,1], [-1,1], points=100000, verbose=True, file="theta.mock.7.F1.png")
fp.cplot(lambda q: F2(q), [-1,1], [-1,1], points=100000, verbose=True, file="theta.mock.7.F2.png")