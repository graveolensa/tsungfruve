#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


a= 3.569945671870944901842005151
def gist(x):
	return a*x*(1-x)

def thue(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		s = 0
		v = euler
		for n in range(1,100):
			if(v<0.5):
				s = s + ((-1)**n)*(q**(2**n))
			else:
				s = s * (1-(q**(3**n)))
			v = gist(v)
		return s/abs(s)

fp.cplot(lambda q: thue(q), [-1,1], [-1,1], points=100000, verbose=True, file="adytum.png")