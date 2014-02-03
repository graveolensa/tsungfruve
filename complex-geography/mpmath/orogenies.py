#!/usr/bin/python
#coding=utf8
import os, sys
from mpmath import *
import mpmath.libmp
import pylab

def l2(q):
	return 1 + fp.nsum(lambda n: q**(2**n), [1,inf])

def l4(q):
	return 1 + fp.nsum(lambda n: q**(4**n), [1,inf])

def quot24(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return l2(q)/l4(q)

def quot42(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		return l4(q)/l2(q)

fp.cplot(lambda q: quot24(q), [-1,1], [-1,1], points=100000, verbose=True, file="quot24.png")
fp.cplot(lambda q: quot42(q), [-1,1], [-1,1], points=100000, verbose=True, file="quot42.png")
