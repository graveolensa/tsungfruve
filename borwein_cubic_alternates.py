#!/usr/bin/python
from mpmath import *
import mpmath.libmp



'''
Borwein Cubic Theta functions a(q), b(q), c(q)
See http://www.math.illinois.edu/REGS/reports10/Schultz.pdf

This file contains two implementations of the Borwein cubic Theta
functions, one a slower double sum (lowercase), and the other
a much faster q-Pochhammer version (capitals)

'''

z = fp.exp(2.0*pi*j/3.0)

'''
a(q) = \newsum_{m,n\in\mathbb{Z}} q^{m^{2}+mn+n^{2}}
'''

def a(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: q**(m*m+ m*n+ n*n), [-inf,inf]), [-inf,inf])
		return A/abs(A)

def A(q):
	if(abs(q)> 1.0):
		return 0.0
	else:
		hack = ( fp.qp(-q,q**2)**2 )*fp.qp(q**2,q**2)*(fp.qp(-q**3,q**6)**2)*fp.qp(q**6,q**6)
		slash = 4.0*q* fp.qp(q**4,q**4)*fp.qp(q**12,q**12)/(fp.qp(q**2,q**4)*fp.qp(q**6,q**12))
		return hack+slash

'''
b(q) = \newsum_{m,n\in\mathbb{Z}} \omega^{m-n}q^{m^{2}+mn+n^{2}}
'''
def b(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: (z**(m-n))*q**(m*m+ m*n+ n*n), [-inf,inf]), [-inf,inf])
		return A/abs(A)

def B(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return (fp.qp(q,q)**3)/fp.qp(q**3,q**3)

'''
c(q) = \newsum_{m,n\in\mathbb{Z}} \omega^q^{(m+1/3)^{2}+(m+1/3)(n+1/3)+(n+1/3)^{2}}
'''


def c(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: q**((m+1/3.0)**2+ (m+1/3.0)*(n+1/3.0)+ ((n+1/3.0)**2)), [-inf,inf]), [-inf,inf])
		return A/abs(A)

def C(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return 3*(q**(1/3.))*(fp.qp(q**3,q**3)**3)/fp.qp(q,q)


