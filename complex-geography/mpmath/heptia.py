#!/usr/bin/python

from mpmath import *
import pylab
import mpmath.libmp

v = 934.0

def u(b):
	return (b-467.0-467.0*j)/467.0

A = u(487.3+459.3*j)
B = u(612.7+443.3*j)
C = u(684.7+525.3*j)
D = u(674.7+622.0*j)
E = u(603.3+681.3*j)
F = u(503.3+673.3*j)
G = u(438+578.7*j)
H = u(323.3+602.7*j)
K = u(293.3+694*j)
L = u(330+758.0*j)
M = u(465.3+759.3*j)
N = u(410+356*j)
O = u(294+360*j)
P = u(230+440*j)
Q = u(240.7 + 538.7*j)

def u(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		Z = (q-A)*(q-B)*(q-C)*(q-D)*(q-E)*(q-F)*(q-G)*(q-H)*(q-K)*(q-L)*(q-M)*(q-N)*(q-O)*(q-P)*(q-Q)
		return Z/abs(Z)

fp.cplot(lambda q: u(q),[-1,1], [-1,1], points=100000, verbose=True, file="heptoid.png")