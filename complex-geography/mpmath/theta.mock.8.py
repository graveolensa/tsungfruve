#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab



'''
Order 8 mock theta functions, See

http://en.wikipedia.org/wiki/Mock_theta_function#CITEREFMcIntosh2007
'''

def S0(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**(n**2))*fp.qp(-q,q*q,n)/fp.qp(-q*q,-q*q,n), [0,inf])
		return out/abs(out)

def S1(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**(n*(n+2)))*fp.qp(-q,q*q,n)/fp.qp(-q*q,q*q,n), [0,inf])
		return out/abs(out)

def T0(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**((n+1)*(n+2)))*fp.qp(-q*q,q*q,n)/fp.qp(-q,q*q,n+1), [0,inf] )
		return out/abs(out)

def T1(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**(n*(n+1)))*fp.qp(-q*q,q*q,n)/fp.qp(-q,q*q,n+1), [0,inf])
		return out/abs(out)

def U0(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out=fp.nsum(lambda n: (q**(n**2))*fp.qp(-q,q*q,n)/fp.qp(-(q**4),q**4,n), [0,inf])
		return out/abs(out)

def U1(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**((n+1)**2))*fp.qp(-q,q*q,n)/fp.qp(-q*q,-(q**4),n+1), [0,inf])
		return out/abs(out)

def V0(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = -1.0 + 2.0*fp.nsum(lambda n: (q**(n**2))*fp.qp(-q,q*q,n)/fp.qp(q,q*q,n), [0,inf])
		return out/abs(out)

def V1(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = fp.nsum(lambda n: (q**((n+1)**2))*fp.qp(-q,q*q,n)/fp.qp(q,q*q,n+1), [0,inf])
		return out/abs(out)

fp.cplot(lambda q: S0(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.S0q.png")
fp.cplot(lambda q: S1(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.S1q.png")
fp.cplot(lambda q: T0(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.T0q.png")
fp.cplot(lambda q: T1(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.T1q.png")
fp.cplot(lambda q: U0(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.U0q.png")
fp.cplot(lambda q: U1(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.U1q.png")
fp.cplot(lambda q: V0(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.V0q.png")
fp.cplot(lambda q: V1(q), [-1,1], [-1,1], points=100000, verbose=True, file ="mock8.V1q.png")