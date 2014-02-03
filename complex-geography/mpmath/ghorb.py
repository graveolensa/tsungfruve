#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

# def g(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: ((q**(7*n+1))-(q**(7*n+4))+(q**(7*n+5))-(q**(7*n)))/(1-(q**(7*n+3))+(q**(7*n+2))), [1,inf])
# 		return A/abs(A)

def g(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		A = fp.nsum(lambda n: ((q**(7*n+q**n))-(q**(7*n+4*(q**n)))+(q**(7*n+5*(q**n)))-(q**(7*n)))/(1-(q**(7*n+3*(q**n)))+(q**(7*n+2*(q**n)))), [1,inf])
		return A/abs(A)



fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=10000000, dpi=400, verbose=True, file="genar.png")