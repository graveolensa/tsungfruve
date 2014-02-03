#!/usr/bin/python
from mpmath import *
import pylab
import mpmath.libmp

def f(z):
  if(abs(z)>1.0):
    return 0.0
  else:
  	z = z/abs(z) * (1-(1-abs(z))**4)
  	r = nsum(lambda n: z**(2**n), [1,inf])
  	return r/abs(r)
  
fp.cplot(lambda z: f(z), [-1,1], [-1,1], points=10000000, dpi=400, file="refalter.png")