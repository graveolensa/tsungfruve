#!/usr/bin/python
from mpmath import *
import colorsys

#input and output files
oddprimes = open('source.list', 'r')
outtable = open('outtable.pnm', 'w')

# Define some colors:

red = '255 0 0\n'
green = '0 255 0\n'
blue = '0 0 255\n'
grey = '128 128 128\n'

# definition of the Legendre Symbol
# See http://mathworld.wolfram.com/LegendreSymbol.html

def legendre(a,p):
	return ((a**((p-1)/2)) % p)


outtable.write('P3\n1369 1369\n256\n')

for line in oddprimes:
	p = int(line)
	for a in range(0,1369):
		if((a>=0)&(a<p)):
			if(legendre(a,p)==1):
				outtable.write(blue)
			if(legendre(a,p)==0):
				outtable.write(green)
			if(legendre(a,p)==p-1):
				outtable.write(red)
		else:
			outtable.write(grey)

outtable.close()
oddprimes.close()
