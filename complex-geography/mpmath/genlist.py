#!/usr/bin/python

from mpmath import *



for a in range(0,2):
    for b in range(0,2):
        for c in range(0,2):
            for d in range(0,2):
                for e in range(0,2):
                    for f in range(0,2):
                        for g in range(0,2):
                            for h in range(0,2):
                                for i in range(0,2):
                                    for w in range (0,2):
                                        q = sqrt(3+(-1*a)*sqrt(3+(-1*b)*sqrt(3+(-1*c)*sqrt(3+(-1*d)*sqrt(3+(-1*e)*sqrt(3+(-1*f)*sqrt(3+(-1*g)*sqrt(3+(-1*h)*sqrt(3+(-1*i)*sqrt(3+(-1*w)*sqrt(3)))))))))))
                                        S = w*(2**9) + i*(2**8) + h*(2**7) + g*(2**6) + f*(2**5) + e*(2**4) +  d*(2**3) + c*(2**2) + a*(2**1) + b*(2**0)
                                        C = S / 1024.0;
                                        print C,q
