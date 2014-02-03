#!/usr/bin/python
from mpmath import *
import pylab

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - ( (q**(n**2))+ (q**(2**n)))/(1-q**(2**n)), [1,inf])
# 		return A/abs(A)

# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="altair.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - ( (q**(n**3))+ (q**(3**n)))/(1-q**(3**n)), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="deneb.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - ( (q**(n**3))- (q**(3**n)))/(1-q**(3**n)), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="fomalhaut.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: (q**(7**n))*(1-(q**(n**5))) / ((1-(q**(n**3)))*(1-(q**(5**n)))), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="polaris.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: ( (q**(3**n)) + (q**(5**n)) + (q**(7**n)) ) / ((1-(q**(n**3)))*(1-q**(n**5))*(1-(q**(n**7)))), [1,inf]) 
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="betelguese.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: ( (q**(3**n)) - (q**(5**n)) + (q**(7**n)) ) / ((1-(q**(n**3)))*(1-q**(n**5))*(1-(q**(n**7)))), [1,inf]) 
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="markab.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: ((-1)**n)*(q**(2**n))/ ((1-(q**(n**3)))*(1-q**(n**5))*(1-(q**(n**7)))), [1,inf]) 
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="menkar.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: (q**(n**3))*((1-q**n)**(1/7.0))/ ((1-(q**(n**3)))*(1-q**(n**5))*(1-(q**(n**7)))), [1,inf]) 
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="merak.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: (q**(3**n))*((1-q**n)**(1/7.0))/ ((1-(q**(n**3)))*(1-q**(n**5))*(1-(q**(n**7)))), [1,inf]) 
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="mekbuda.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: (q**(n**3))*((1-q**n)**(1/7.0))/ ((1-(q**(3**n)))*(1-q**(5**n))*(1-(q**(7**n)))), [1,inf]) 
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="arcturus.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nsum(lambda n: ((-1)**n)*(q**(3*n*n+5*n+7))/ ((1-(q**(3**n)))*(1-q**(5**n))*(1-(q**(7**n)))), [1,inf]) 
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="aldebaran.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - (q**(n**3))*((1-q**n)**(1/7.0)), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="rukbat.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - (q**(3**n))*((1-q**n)**(1/7.0)), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="rastaban.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - (q**(n**3))*((1-q**(n**3))**(1/3.0)), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="sabik.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - (q**(7**n))*((1-q**(7**n))**(1/7.0)), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="risha.png")

# def g(q):
# 	if(abs(q)>=1.0):
# 		return 0.0
# 	else:
# 		A = fp.nprod(lambda n: 1.0 - q**(n**3 + 7*n + 2), [1,inf])
# 		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="rasalased.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: (q**n)*fp.qp(q**(n**2),q**(2**n))/( (1-(q**(n**2)))*(1-(q**(2**n)))), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="azmidiske.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: (q**n)*fp.qp(q**(2**n),q**(n**2))/( (1-(q**(n**2)))*(1-(q**(2**n)))), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="azpidiske.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nprod(lambda n: (q**n)*fp.qp(q**(2**n),q**(n**2))/( (1-(q**(n**2)))*(1-(q**(2**n)))), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="azpidiske.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nprod(lambda n: (q**n)*fp.qp(q**(2**n),q**(n**2))/( (1-(q**(n**2)))*(1-(q**(2**n)))), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="azpidiske.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nprod(lambda n: (fp.qp(q**(n**2),q**(2**n))* fp.qp(q**(3**n),q**(n**3)))/(fp.qp(q**(2**n),q**(n**2))* fp.qp(q**(n**3),q**(3**n))), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="alphecca.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: ((-1)**n)*(q**(n**2))/(1-(q**(2**n))+q**(n**2)), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="wasat.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: ((-1)**n)*(q**(n**2))/(1+(q**(2**n))-q**(n**2)), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="wesen.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: ((-1)**n)*(q**(n**3))/(1+(q**(3**n))-q**(n**3)), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="thuban.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: ((-1)**n)*(q**(3**n))/(1+(q**(3**n))-q**(n**3)), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="unuqathai.png")

# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: ((-1)**n)*(q**(n**3))/(1+(q**(3**n))-q**(n**3)), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="sirrah.png")


# v = fp.exp(pi * j * fp.sqrt(7))
# r = fp.exp(pi * j * 3.0**(1/7.0))
# def g(q):
#  	if(abs(q)>=1.0):
#  		return 0.0
#  	else:
#  		A = fp.nsum(lambda n: (q**(n**3.0))*(v**n)/(1.0 + (q**(n**7)) - (q**(4**n))*(r**n)), [1,inf])
#  		return A/abs(A)
		
# fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="sadalbari.png")

def g(q):
	if(abs(q)>=1.0):
		return 0.0
	else:
		A = fp.nsum(lambda n: ((-1)**n)*q**(3.0*n*n+2.0*n+3.0), [1,inf])
		return A/abs(A)

fp.cplot(lambda q: g(q), [-1,1], [-1,1], points=100000, verbose=True, file="centauri.png")