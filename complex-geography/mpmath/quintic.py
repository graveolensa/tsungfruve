#!/usr/bin/python
from mpmath import *
import mpmath.libmp
import pylab

'''
quintic theta functions. 
See Tim Huber's paper:
http://arxiv.org/pdf/1304.0684v1.pdf
/A Theory of Theta Functions to a Quintic Base/
'''


# declare the fifth root of unity
r = fp.exp(2.0 * pi * j / 5.0)
# makes computation of C(q) faster:
r3 = r**3.0

# def A(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		out = (q**(1/5.0))*((fp.qp(q,q))**(-3.0/5.0))*fp.nsum(lambda n: ((-1)**n)*(q**((5*n*n-3*n)/2.0)), [-inf,inf])
# 		return out/abs(out)

# evaluated way too fast, have to try it again.
# def B(q):
# 	if(abs(q)>1,0):
# 		return 0.0
# 	else:
# 		out = (fp.qp(q,q)**(-3.0/5.0))*fp.nsum(lambda n: ((-1)**n)*(q**((5*n*n-n)/2.0)), [-inf,inf])
# 		return out/abs(out)

def B(q):
	if(abs(q)>1.0):
		return 0.0
	else:
		out = (fp.qp(q,q)**(-3.0/5.0)) * fp.nsum(lambda n: ((-1)**n)*(q**((5*n*n-n)/2.0)), [-inf,inf])
		return out/abs(out)

# def C(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		out = ((fp.qp(q**5,q**5))**(-3.0/5.0))*fp.nsum(lambda n: (r3**n)*(q**((n*n-n)/2.0)), [-inf,inf])/(1+r3)
# 		return out/abs(out)

# def D(q):
# 	if(abs(q)>1.0):
# 		return 0.0
# 	else:
# 		out = ((fp.qp(q**5,q**5))**(-3.0/5.0))*fp.nsum(lambda n: (r**n)*(q**((n*n-n)/2.0)), [-inf,inf])/(1+r)
# 		return out/abs(out)

# fp.cplot(lambda q: A(q), [-1,1], [-1,1], points=100000, verbose=True, file="quinticAq.png")
fp.cplot(lambda q: B(q), [-1,1], [-1,1], points=100000, verbose=True, file="quinticBq.png")
# fp.cplot(lambda q: C(q), [-1,1], [-1,1], points=100000, verbose=True, file="quinticCq.png")
# fp.cplot(lambda q: D(q), [-1,1], [-1,1], points=100000, verbose=True, file="quinticDq.png")