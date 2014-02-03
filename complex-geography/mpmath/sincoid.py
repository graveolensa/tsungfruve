#!/usr/bin/python
from mpmath import *
import pylab

'''
q-deformed version of Viete's product

replacing the (1/2^n) with q^n term
'''

def g(q,thet):
	if(abs(g)>1.0):
		return 0.0
	else:
		a = fp.nprod(lambda n: fp.cos((q**n)*thet), [1,inf])
		return a/abs(a)

'''
the logical movie to make here runs from 
0 through 2pi in 1024 steps, and when I get
some more disk space I might think of
rendering this
'''

theet = pi/7.0

fp.cplot(lambda : g(q,theet), [-1,1], [-1,1], points=20000000, verbose=True, file="viete7.png")