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

def eleven(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A =11.0
		return A/abs(A)

def one(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = 1.0
		return A/abs(A)

# this is just defined this way so that one may keep one's sanity.
def fquot(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A=fp.qp(-q,-q)
		return A/abs(A)

def qonefifth(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = q**(1/5)
		return A/abs(A)

def qfifth(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A=q**5
		return A/abs(A)

def Q(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return q/abs(q)

fp.cplot(lambda q: R(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.Rq.svg")
fp.cplot(lambda q: -R(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.minusRq.svg")
fp.cplot(lambda q: 1/R(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.recipRq.svg")
fp.cplot(lambda q: -R(q)**5, [-1,1], [-1,1], points=100000, verbose=True, file="rogram.minusRq5.svg")
fp.cplot(lambda q: 1/(R(q)**5), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.recipRq.svg")
fp.cplot(lambda q: one(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.oneq.svg")
fp.cplot(lambda q: -one(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.minusoneq.svg")
fp.cplot(lambda q: eleven(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.elevenq.svg")
fp.cplot(lambda q: -eleven(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.minuselvenq.svg")
fp.cplot(lambda q: fquot(-q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.fquot.svg")

fp.cplot(lambda q: fquot(-q)**6, [-1,1], [-1,1], points=100000, verbose=True, file="rogram.fquotsixth.svg")

fp.cplot(lambda q: fquot(-(q**5)**6), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.fquotfifthsixth.svg")
fp.cplot(lambda q: fquot(-(q**(1/5))), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.fquotq1over5.svg")

fp.cplot(lambda q: fquot(-(q**5)), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.fqfifth.svg")
fp.cplot(lambda q: fquot(-(q**(1/5))), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.fquotq1over5.svg")

fp.cplot(lambda q: 1/(R(q)) -1.0 - R(q), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.LHS.1.svg")
fp.cplot(lambda q: fquot(-q**(1/5))/(q**(1/5)*fquot(-q**5)), points=100000, verbose=True, file="rogram.RHS.1.svg")

fp.cplot(lambda q: 1/(R(q)**5) -11.0 - R(q)**(5), [-1,1], [-1,1], points=100000, verbose=True, file="rogram.LHS.2.svg")
fp.cplot(lambda q: (fquot(-q)**6)/(q*(fquot(-q**5)**6)), points=100000, verbose=True, file="rogram.RHS.2.svg")