#!/usr/bin/python
from mpmath import *

rho = 2.1 


# assume that we have already calculated the Bring Quintic Form
# and that we have rho already

# compute the elliptic modulus k

K = tan( asin(16.0/(25*sqrt(5)*rho*rho)))

#compute s
if(re(rho)==0.0):
	s = -sign(im(rho))
if(re(rho)!=0.0):
	s = sign(re(rho))

#compute b

b = s*( (K*K)**(1/8.0)) / (2.0 * (5.0**(3.0/4.0)) * sqrt(K*(1-K*K)))

# Compute the nome in terms of the elliptic modulus
# fortunately mpmath provides a utility function that does this.

q = qfrom(k=K)

def m(Q):
	V = (jtheta(2,0,Q)/jtheta(3,0,Q))**4.0
	return V


#compute fifth root of q to make life easier

qr = q**(1/5.0)
q5 = q**(5.0)

root1 = (exp(3*pi*j/4.0) ) * b * ( m( exp(-2*pi*j/5.0) * qr)**(1/8.0) + j* m( exp(2*pi*j/5.0) * qr)**(1/8.0)) * (m( exp(-4*pi*j/5.0) * qr)**(1/8.0) + m( exp(4*pi*j/5.0) * qr)**(1/8.0)) * (m(qr)**(1/8.0) + m(q5)**(1/8.0))

print root1
