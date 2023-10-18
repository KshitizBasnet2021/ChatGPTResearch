
"""
llllllIIIl


Input:
    IlIlIIIlIIl: A list of unique ints

Precondition:
    IlIlIIIlIIl is not sorted in reverse order

Output:
    The lexicographically next permutation of the elements of IlIlIIIlIIl

Example:
    >>> llllllIIIl([3, 2, 4, 1])
    [3, 4, 1, 2]
"""

def llllllIIIl(IlIlIIIlIIl):
    for IIIlIlIlI in range(len(IlIlIIIlIIl) - 2, -1, -1):
        if IlIlIIIlIIl[IIIlIlIlI] < IlIlIIIlIIl[IIIlIlIlI + 1]:
            for lIlIIIIlIIlIIIIlII in range(len(IlIlIIIlIIl) - 1, IIIlIlIlI, -1):
                if IlIlIIIlIIl[lIlIIIIlIIlIIIIlII] < IlIlIIIlIIl[IIIlIlIlI]:
                    IIllIllIIIlI = list(IlIlIIIlIIl)
                    IIllIllIIIlI[IIIlIlIlI], IIllIllIIIlI[lIlIIIIlIIlIIIIlII] = IlIlIIIlIIl[lIlIIIIlIIlIIIIlII], IlIlIIIlIIl[IIIlIlIlI]
                    IIllIllIIIlI[IIIlIlIlI + 1:] = reversed(IIllIllIIIlI[IIIlIlIlI + 1:])
                    return IIllIllIIIlI