#!/usr/bin/python
from mpmath import *
import pylab


A = matrix(200,1)
B = matrix(200,1)
C = matrix(200,1)

x = 0.2
y = -2.4
z = 1.1

for u in range(1,198):
	X = 2.0 * fp.cos(z-y)
	Y = 2.0 * fp.sin(x-z)
	Z = 7.0 * fp.cos(y-x)
	A[u]=X
	B[u]=Y
	C[u]=Z
	x = X
	y = Y
	z = Z

def a(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = 0.0
		for n in range(1,100):
			out = out + A[n]*(q**n)
		return out/abs(out)

def b(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = 0.0
		for n in range(1,100):
			out = out + B[n]*(q**n)
		return out/abs(out)

def c(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = 0.0
		for n in range(1,100):
			out = out + C[n]*(q**n)
		return out/abs(out)


fp.cplot(lambda q: a(q), [-1,1], [-1,1], points=100000, verbose=True, file="xweird.png")
fp.cplot(lambda q: b(q), [-1,1], [-1,1], points=100000, verbose=True, file="yweird.png")
fp.cplot(lambda q: c(q), [-1,1], [-1,1], points=100000, verbose=True, file="zweird.png")