#!/usr/bin/python
from mpmath import *
import pylab

def s(z):
	return (1-fp.sin(z**3)**2)/(1+fp.cos(z**2)**3)

def anewt(z):
	a = 0.0
	for u in range(1,100):
		S = s(z)
		a = a + s**(u-s**(u-s))
		''' save us some time '''
		mc = fp.cos(z**2)
		ms = fp.sin(z**3)
		uc = fp.cos(z**3)
		us = fp.sin(z**2)
		z = z - S/( (-6*z*uc* (z*ms+ z*ms*(mc**3) -us*uc*(mc**2)))/( (1+mc**3)**2))
	return a/abs(a)

fp.cplot(lambda z: anewt(z), [-5,5], [-5,5], points=20000000, dpi=400, verbose=True, file="wildefaar.png")