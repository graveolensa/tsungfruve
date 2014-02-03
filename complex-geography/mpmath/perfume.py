#!/usr/bin/python

from mpmath import *

# initial values

a = 0.01
b = j/37.0
z = 0.4
w = -3.1
Q = 0.003*j;
x = 0.1
y = 2.1
w = 0.01;

for i in range(0, 1000):
    X = fp.jtheta(1,2*cos(z-y),Q)
    Y = fp.jtheta(2,2*sin(x-z)+2*cos(w-z),Q)
    Z = fp.jtheta(3,7*cos(y-x)+2*sin(y-w),Q)
    W = fp.jtheta(4,cos(z-y),Q)
    Q = conj(Q)
    x = X
    y = Y
    z = Z
    w = W
    print x,y,z,w
