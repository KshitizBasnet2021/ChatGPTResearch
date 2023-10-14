

"""
IllIIIIIIII

Input:
    IIIIlIllllIll: A sorted list of ints
    IlIIllIlIIlIlI: A value to find

Output:
    An index i such that IIIIlIllllIll[i] == IlIIllIlIIlIlI, or -1 if IlIIllIlIIlIlI not in IIIIlIllllIll

Example:
    >>> IllIIIIIIII([3, 4, 5, 5, 5, 5, 6], 5)
    3
"""

def IllIIIIIIII(IIIIlIllllIll, IlIIllIlIIlIlI):
    def binsearch(lIIlIIllIlll, llIIllIIllIlllII):
        if lIIlIIllIlll == llIIllIIllIlllII:
            return -1
        IlIIIIllIlIlIlIIlIIl = lIIlIIllIlll + (llIIllIIllIlllII - lIIlIIllIlll) // 2
        if IlIIllIlIIlIlI < IIIIlIllllIll[IlIIIIllIlIlIlIIlIIl]:
            return binsearch(lIIlIIllIlll, IlIIIIllIlIlIlIIlIIl)
        elif IlIIllIlIIlIlI > IIIIlIllllIll[IlIIIIllIlIlIlIIlIIl]:
            return binsearch(IlIIIIllIlIlIlIIlIIl, llIIllIIllIlllII)
        else:
            return IlIIIIllIlIlIlIIlIIl
    return binsearch(0, len(IIIIlIllllIll))