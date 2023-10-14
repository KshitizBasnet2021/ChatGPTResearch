
"""
IlIIllll


Input:
    lIllIlllI: A sequence of ints

Precondition:
    The ints in lIllIlllI are unique

Output:
    The length of the longest monotonically increasing subsequence of lIllIlllI

Example:
    >>> IlIIllll([4, 1, 5, 3, 7, 6, 2])
    3
"""

def IlIIllll(lIllIlllI):
    lIIIlllIIlIIIIIIl = {}
    llIIIlIll = 0
    for IlllIIIIlIllllIllll, IIllIllIlIlllllIl in enumerate(lIllIlllI):
        lIIlIIII = [IlIllllIllIlllllIlll for IlIllllIllIlllllIlll in range(1, llIIIlIll + 1) if lIllIlllI[lIIIlllIIlIIIIIIl[IlIllllIllIlllllIlll]] < IIllIllIlIlllllIl]
        lIIIIIllIllII = max(lIIlIIII) if lIIlIIII else 0
        if lIIIIIllIllII == llIIIlIll or IIllIllIlIlllllIl < lIllIlllI[lIIIlllIIlIIIIIIl[lIIIIIllIllII + 1]]:
            lIIIlllIIlIIIIIIl[lIIIIIllIllII + 1] = IlllIIIIlIllllIllll
            llIIIlIll = lIIIIIllIllII + 1
    return llIIIlIll