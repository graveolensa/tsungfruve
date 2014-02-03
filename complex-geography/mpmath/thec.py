#/usr/bin/python
import mpmath
from mpmath import mpf
mpmath.mp.pretty=True

def zeta3test():

    n=3
    mpmath.mp.dps=10^3
    zeta3=mpmath.zeta(3)

    Pi=mpmath.pi
    gamma=mpmath.euler
    z12=mpmath.zeta(1/mpmath.mpf(2))
    z1=mpmath.zeta(1/mpmath.mpf(2),derivative=1)
    z2=mpmath.zeta(1/mpmath.mpf(2),derivative=2)
    z3=mpmath.zeta(1/mpmath.mpf(2),derivative=3)

    # eliminate the first derivative

    #rh0=1/32*(72*Pi*mpmath.log(2)*mpmath.log(Pi)*z12+144*gamma*mpmath.log(2)*mpmath.log(Pi)*z12+72*mpmath.log(2)*z12*gamma*Pi+24*mpmath.log(Pi)*z12*gamma*Pi-144*z2*mpmath.log(2)-48*z2*mpmath.log(Pi)+216*mpmath.log(2)^3*z12+8*mpmath.log(Pi)^3*z12-48*z2*gamma-24*z2*Pi+8*z12*gamma^3+z12*Pi^3+72*mpmath.log(2)*z12*gamma^2+18*mpmath.log(2)*z12*Pi^2+24*mpmath.log(Pi)*z12*gamma^2+6*mpmath.log(Pi)*z12*Pi^2+216*mpmath.log(2)^2*mpmath.log(Pi)*z12+72*mpmath.log(2)*mpmath.log(Pi)^2*z12+216*gamma*mpmath.log(2)^2*z12+24*gamma*mpmath.log(Pi)^2*z12+108*Pi*mpmath.log(2)^2*z12+12*Pi*mpmath.log(Pi)^2*z12+32*z3+12*z12*gamma^2*Pi+6*z12*gamma*Pi^2)/z12
    z12a=mpmath.fabs(z12)
    rh1= -z3/z12a -3*z2*z1/z12a**2 -2* z1**3/z12a**3

    #print 'rh',mpmath.chop(rh0-rh1)
    #rhs= (mpmath.diff( lambda y:  mpmath.log(mpmath.fabs(mpmath.zeta(y))),1/2,n) - mpmath.pi^3 / 4 )/(7)
    rhs= (rh1 - mpmath.pi**3 / 4 )/(7)
    print mpmath.chop(zeta3-rhs)

def conjecture1(n):
    """

    voros, p. 12
    """
    assert n%2==1
    a1= mpmath.zeta(n)
    a2= (2/factorial(n-1) * mpmath.diff( lambda y:  mpmath.log(mpmath.fabs(mpmath.zeta(y))),1/2,n) - 2**(n) * dirichletbeta(n))/(2**n-1)
    print mpmath.chop(a1-a2)


def dirichletbeta(s):
    """
    dirichlet beta
    """
    return 4**(-s) * (mpmath.hurwitz(s,1/4)-mpmath.hurwitz(s,3/4))

