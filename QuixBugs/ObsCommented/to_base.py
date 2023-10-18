
"""
IllIIllIIIlIIlIlll


Input:
    llIllIlllIIIIIllIIl: A base-10 integer to convert.
    IIlIlIllIIl: The target base to convert it to.

Precondition:
    llIllIlllIIIIIllIIl > 0, 2 <= IIlIlIllIIl <= 36.

Output:
    A string representing the value of llIllIlllIIIIIllIIl in base b.

Example:
    >>> IllIIllIIIlIIlIlll(31, 16)
    '1F'
"""

import string
def IllIIllIIIlIIlIlll(llIllIlllIIIIIllIIl, IIlIlIllIIl):
    IIIlIllIIlIllIIlIl = ''
    IllIIIIIIlIlI = string.digits + string.ascii_uppercase
    while llIllIlllIIIIIllIIl > 0:
        llIIIIIl = llIllIlllIIIIIllIIl % IIlIlIllIIl
        llIllIlllIIIIIllIIl = llIllIlllIIIIIllIIl // IIlIlIllIIl
        IIIlIllIIlIllIIlIl = IIIlIllIIlIllIIlIl + IllIIIIIIlIlI[llIIIIIl]
    return IIIlIllIIlIllIIlIl