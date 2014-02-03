#!/usr/bin/python
from mpmath import *
import pylab

def rhumb(t):
	s = 1.0
	m = fp.kleinj(tau=t)
	for u in range(1,100):
		s = s * (m**(3*u)-3*m**(u) +1)/(m**(2*u)+j*m**(u) +1)
	return s/abs(s)

fp.cplot(lambda z: rhumb(z), [0.000001,1], [-1,1], points=20000000, dpi=400, verbose=True, file="mharga.png")
