#!/usr/bin/python

from mpmath import *
import pylab

def f(z):
	return fp.cos(abs(z))-tan(z*z)+exp(1)

fp.cplot(lambda q: f(q), [-10,10], [-10,10], verbose=True, points=200000, file="lemuel.png")