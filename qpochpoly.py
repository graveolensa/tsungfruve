#!/usr/local/bin/python3
from mpmath import *
import mpmath.libmp
import pylab



L = matrix(1,40)
for u in range(1,40):
	L[u] = rand()* exp(2*pi* j * rand())
	print(L[u])

def A(z):
	out = 0.0
	if(abs(z)>1.0):
		out = 0.0
	else:
		out = 1.0
		for p in range(1,20):
			v = L[p]
			out = out * (1.0 - z/v);
		out = out/abs(out)
	return out


def B(z):
	if(abs(z)>1.0):
		out = 0.0
	else:
		out = 1.0
		for p in range(1,20):
			v = L[p]
			out = out * fp.qp(1.0/v,z)
		out = out/abs(out)
	return out

fp.cplot(lambda z: A(z), [-1.001,1.001], [-1.001,1.001], points=20000000,dpi=400,verbose=True, file="unitpoly.png")
fp.cplot(lambda z: B(z), [-1.001,1.001], [-1.001,1.001], points=20000000,dpi=400,verbose=True, file="unitmod.png")
