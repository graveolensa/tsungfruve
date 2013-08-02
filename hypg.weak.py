#!/usr/bin/python
from mpmath import *

def F1(t):
	return hyper([-1/20.0 , 3/20.0 , 7/20.0 , 11/20.0], [1/4.0 , 1/2.0 , 3/4.0], 3125*(t**4)/256)

def F2(t):
	return hyper([1/5.0 , 2/5.0 , 3/5.0 , 4/5.0], [1/2.0 , 3/4.0 , 5/4.0], 3125*(t**4)/256)

def F3(t):
	return hyper([9/20.0 , 13/20.0 , 17/20.0 , 21/20.0], [3/4.0 , 5/4.0 , 3/2.0], 3125*(t**4)/256)

def F4(t):
	return hyper([7/10.0 , 9/10.0 , 11/10.0, 13/10.0], [5/4.0 , 3/2.0 , 7/4.0], 3125*(t**4)/256)


def x1(t):
	return t*F2(t)

def x2(t):
	return -(-F1(t) + (t/4)*F2(t) + (5*t*t/32)*F3(t) + (5*t*t*t/32) * F4(t))


def x3(t):
	return -(F1(t) + (t/4)*F2(t) - (5*t*t/32)*F3(t) + (5*t*t*t/32) * F4(t))


def x4(t):
	return -(-j*F1(t) + (t/4)*F2(t) -(5*t*t/32)*j*F3(t) - (5*t*t*t/32) * F4(t))

def x5(t):
	return -(j*F1(t) + (t/4)*F2(t) +(5*t*t/32)*j*F3(t) - (5*t*t*t/32) * F4(t))

#T =  sqrt((16/(25*sqrt(5)))*sqrt(8/(5-sqrt(5))))
T = -sqrt(7)*j +1

mp.dps=30

print limit(lambda u: x1(u), T)
print limit(lambda u: x2(u), T)
print limit(lambda u: x3(u), T)
print limit(lambda u: x4(u), T)
print limit(lambda u: x5(u), T)
