#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

'''
order 3 mock theta functions
see http://en.wikipedia.org/wiki/Mock_theta_function
'''

# def f(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		return fp.nsum(lambda n: (q**(n**2))/(fp.qp(-q,q,n)**2.0), [0,inf])


# def phi(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		return fp.nsum(lambda n: (q**(n**2))/(fp.qp(-q*q,q*q,n)), [0,inf])

# def psi(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		return fp.nsum(lambda n: (q**(n**2))/(fp.qp(q,q*q,n)), [0,inf])

# def omega(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		return fp.nsum(lambda n: (q**(2*n*(n+1)))/(fp.qp(q,q*q,n)**2), [0,inf])


def nu(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return fp.nsum(lambda n: (q**(n*(n+1)))/(fp.qp(-q,q*q,n)), [0,inf])

# fp.cplot(lambda q: f(q), [-1,1], [-1,1], points=100000, verbose=True, file="mok.theta.fq.png")
# fp.cplot(lambda q: phi(q), [-1,1], [-1,1], points=100000, verbose=True, file="mok.theta.phiq.png")
# fp.cplot(lambda q: psi(q), [-1,1], [-1,1], points=100000, verbose=True, file="mok.theta.psiq.png")
# fp.cplot(lambda q: omega(q), [-1,1], [-1,1], points=100000, verbose=True, file="mok.theta.omega.png")
fp.cplot(lambda q: nu(q), [-1,1], [-1,1], points=100000, verbose=True, file="mok.theta.nuq.png")