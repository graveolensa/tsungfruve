#!/usr/bin/python
from mpmath import *


# k -> ellmodk
# Get the elliptic modulus k
def ellmodk(rho):
  return tan(asin(16/(25*rho*rho*sqrt(5)))/4.0)

# get the nome from k
def gnome(rho):
	return qfrom(k=ellmodk(rho))

def b(rho):
	k=ellmodk(rho)
	return ((k**2)**(1/8.0))/(2.0*(5**(3.0/4.0))*sqrt(k*(1-k*k)))

def m(q):
	return (jtheta(2,0,q)/jtheta(3,0,q))**4.0

# the utility moo, makes doing all the tedious work much easier
def moo(a,b,rho):
	q = gnome(rho)
	return m(exp(a*pi*j)*(q**b))**(1/8.0)

# utility exponentials
em34 = exp(-3.0*pi*j/4)
em45 = exp(-4.0*pi*j/5)
em25 = exp(-2.0*pi*j/5)
e25 = exp(2.0*pi*j/5)
e45 = exp(4.0*pi*j/5)
e34 = exp(3.0*pi*j/4)

mp.dps=20
# yes
def x1(rho):
	return e34*b(rho) * (moo(-2.0/5.0,1/5.0,rho) + j*moo(2.0/5.0,1.0/5.0,rho)) * (moo(-4.0/5.0,1/5.0,rho) + moo(4.0/5.0,1.0/5.0,rho)) * (moo(2.0,1/5.0,rho) + moo(2.0,5.0,rho))


def x2(rho):
	return b(rho) * (-moo(2.0,1/5.0,rho) + e34*moo(2.0/5.0,1.0/5.0,rho)) * (em34*moo(-2.0/5.0,1/5.0,rho) + j*moo(4.0/5.0,1.0/5.0,rho)) * (j*moo(-4.0/5.0,1/5.0,rho) + moo(2.0,5.0,rho))

# yes, modulo minus sign
def x3(rho):
	return b(rho) * (em34*moo(-2.0/5.0,1/5.0,rho) - j*moo(-4.0/5.0,1.0/5.0,rho)) * (-moo(2.0,1/5.0,rho) - j*moo(4.0/5.0,1.0/5.0,rho)) * (e34*moo(2.0/5.0,1/5.0,rho) + moo(2.0,5.0,rho))

# yes!
def x4(rho):
	return b(rho) * (moo(2.0,1/5.0,rho) - j*moo(-4.0/5.0,1.0/5.0,rho)) * (-e34*moo(2.0/5.0,1/5.0,rho) - j*moo(4.0/5.0,1.0/5.0,rho)) * (em34*moo(-2.0/5.0,1/5.0,rho) + moo(2.0,5.0,rho))


#yes
def x5(rho):
	return b(rho) * (moo(2.0,1/5.0,rho) -em34*moo(-2.0/5.0,1.0/5.0,rho)) * (-e34*moo(2.0/5.0,1/5.0,rho) + j*moo(-4.0/5.0,1.0/5.0,rho)) * (-j*moo(4.0/5.0,1/5.0,rho) + moo(2.0,5.0,rho))

arr = 4.0/(5.0**(5.0/4.0))

print x1(arr)
print x2(arr)
print x3(arr)
print x4(arr)
print x5(arr)
