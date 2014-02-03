#!/usr/bin/python
from mpmath import *

'''
determine rational convergents to the first zeta zero
mpc(real='0.5', imag='14.13472514173469379045725198356247027078425711569924317568556746014996342980925676494901039317156101283')

initial value is 1/2 + 14i
Newton's method has quadratic convergence.

stage 1: we need the absolute values of the differences of Newton's method
convergents. These are likely to be pretty small numbers. 

stage 2: choose disks for each convergent such that each disk only
contains this current convergent and not the next -- disjoint disks

stage 3: select a rational number within each disk of low denominator
stage 3 requires some perturbation: we want to find interesting
families of rational representations of the roots

-> observation: we know that the real convergents must converge to 1/2, which
gives us a starting point for finding the complex convergent with smallest denominator, but
it also means we can sort of force which rational complex values we're using, if we've got
a sequence of 1/2 + 1/n^(2). Newton's method or other rootfinding methods are likely
to have the real term go to 1/2 extremely fast, which is going to mean that many
decimal places are likely to be required, and also means that we have to be
really quite careful about the denominators. 

-> once we have an infinite sum in positive terms for zetazero(1) of smallest
possible denominator in a variety of rootfinding methods, it kind of makes sense
to hunt around for a representation which is meaningful to the zeta function itself ->
we have many many choices to make for both rootfinding method and perhaps to ask
what are its combinatorics? Once we have a representation in a series of rational
terms, we can massage the representation into others.

'''


''' preliminary experiments would seem to indicate that Newton's method
actually converges *too fast*
