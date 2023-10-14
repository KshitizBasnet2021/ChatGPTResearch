
"""
IlIlIIIIIlllII


Input:
    IllIlllIIIIl: A sorted list of ints
    llIlllIIII: A value to find

Output:
    The lowest index i such that IllIlllIIIIl[i] == llIlllIIII, or -1 if llIlllIIII not in IllIlllIIIIl

Example:
    >>> IlIlIIIIIlllII([3, 4, 5, 5, 5, 5, 6], 5)
    2
"""

def IlIlIIIIIlllII(IllIlllIIIIl, llIlllIIII):
    IlIllllIIlIIIIIl = 0
    IlIIIllllllIIIlll = len(IllIlllIIIIl)
    while IlIllllIIlIIIIIl <= IlIIIllllllIIIlll:
        IlIIlllllIlllI = (IlIllllIIlIIIIIl + IlIIIllllllIIIlll) // 2
        if llIlllIIII == IllIlllIIIIl[IlIIlllllIlllI] and (IlIIlllllIlllI == 0 or llIlllIIII != IllIlllIIIIl[IlIIlllllIlllI - 1]):
            return IlIIlllllIlllI
        elif llIlllIIII <= IllIlllIIIIl[IlIIlllllIlllI]:
            IlIIIllllllIIIlll = IlIIlllllIlllI
        else:
            IlIllllIIlIIIIIl = IlIIlllllIlllI + 1
    return -1