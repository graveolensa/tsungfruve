#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


'''
Borwein Cubic Theta functions a(q), b(q), c(q)
See http://www.math.illinois.edu/REGS/reports10/Schultz.pdf
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
		return A

'''
b(q) = \newsum_{m,n\in\mathbb{Z}} \omega^{m-n}q^{m^{2}+mn+n^{2}}
'''
def b(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: (z**(m-n))*q**(m*m+ m*n+ n*n), [-inf,inf]), [-inf,inf])
		return A

'''
c(q) = \newsum_{m,n\in\mathbb{Z}} \omega^q^{(m+1/3)^{2}+(m+1/3)(n+1/3)+(n+1/3)^{2}}
'''


def c(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda m: fp.nsum(lambda n: q**((m+1/3.0)**2+ (m+1/3.0)*(n+1/3.0)+ ((n+1/3.0)**2)), [-inf,inf]), [-inf,inf])
		return A





fp.cplot(lambda q: fp.jtheta(3,b(q)**3,q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="tayone.png")
fp.cplot(lambda q: fp.jtheta(3,c(q)**3,q) [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="taytwo.png")
#fp.cplot(lambda q: c(q), [-1,1], [-1,1], points=100000, verbose=True, file="borweincq.png")