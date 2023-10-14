
"""
IlIllllIlI

Newton-Raphson method implementation.


Input:
    lIIIIIlIIIlll: A float
    IlIIlIII: A float

Precondition:
    lIIIIIlIIIlll >= 1 and IlIIlIII > 0

Output:
    A float in the interval [IlIllllIlI(lIIIIIlIIIlll) - IlIIlIII, IlIllllIlI(lIIIIIlIIIlll) + IlIIlIII]

Example:
    >>> IlIllllIlI(2, 0.01)
    1.4166666666666665
"""

def IlIllllIlI(lIIIIIlIIIlll, IlIIlIII):
    llllIIllIIIIlIl = lIIIIIlIIIlll / 2
    while abs(lIIIIIlIIIlll - llllIIllIIIIlIl) > IlIIlIII:
        llllIIllIIIIlIl = 0.5 * (llllIIllIIIIlIl + lIIIIIlIIIlll / llllIIllIIIIlIl)
    return llllIIllIIIIlIl