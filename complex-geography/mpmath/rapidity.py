#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

''' 
visual exploration of the rogers ramanujan continued fraction identities
Owen Maresh, 2013
'''

def R(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = (q**(1/5.0))*fp.qp(q,q**5)*fp.qp(q**4,q**5)/(fp.qp(q**2,q**5)*fp.qp(q**3,q**5))
		return A/abs(A)

def z(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.qp(q,q**5)
		return A/abs(A)

def x(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.qp(q**4,q**5)
		return A/abs(A)


def c(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.qp(q**2,q**5)
		return A/abs(A)

def v(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.qp(q**3,q**5)
		return A/abs(A)

def slf(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = q
		return A/abs(A)

def sq(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = q*q
		return A/abs(A)

def cb(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = q*q*q
		return A/abs(A)


def quar(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = q*q*q*q
		return A/abs(A)

def quin(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = q*q*q*q*q
		return A/abs(A)

def niuq(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = q**(1/5.0)
		return A/abs(A)

# fp.cplot(lambda q: R(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.Rq.svg")
# fp.cplot(lambda q: z(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.zq.svg")
# fp.cplot(lambda q: x(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.xq.svg")
# fp.cplot(lambda q: c(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.cq.svg")
# fp.cplot(lambda q: v(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.vq.svg")

# fp.cplot(lambda q: slf(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.slfq.svg")
# fp.cplot(lambda q: sq(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.sq.svg")
# fp.cplot(lambda q: cb(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.cbq.svg")
# fp.cplot(lambda q: quar(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.quarq.svg")
fp.cplot(lambda q: quin(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.quinq.svg")
fp.cplot(lambda q: niuq(q), [-1,1], [-1,1], points=100000, verbose=True, file="vis.niuqq.svg")