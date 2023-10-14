
"""
Input:
    IIlIIIIIIIIIlIIIIl: A nonnegative int
    lIlIIIlIIllII: A nonnegative int


Greatest Common Divisor

Precondition:
    isinstance(IIlIIIIIIIIIlIIIIl, int) and isinstance(lIlIIIlIIllII, int)

Output:
    The greatest int that divides evenly into IIlIIIIIIIIIlIIIIl and lIlIIIlIIllII

Example:
    >>> IlIIlllllIII(35, 21)
    7

"""

def IlIIlllllIII(IIlIIIIIIIIIlIIIIl, lIlIIIlIIllII):
    if lIlIIIlIIllII == 0:
        return IIlIIIIIIIIIlIIIIl
    else:
        return IlIIlllllIII(IIlIIIIIIIIIlIIIIl % lIlIIIlIIllII, lIlIIIlIIllII)