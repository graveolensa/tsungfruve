#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab


mp.dps=10
for u in range(0,100):
	for v in range(0,100):
		for w in range(0,100):
			u = u*0.01
			v = v*0.01
			w = w*0.01

			u1 = u+0.005
			v1 = v+0.005
			w1 = w+0.005
			print u ,v ,w
			print u,v1,w1
			print u1,v,w1
			print u1,v1,w