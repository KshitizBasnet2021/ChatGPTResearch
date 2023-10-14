
"""
IIIlIlIlIIIII

Input:
    lIIllIIIIlIlI: A list

Precondition:
    lIIllIIIIlIlI has no duplicate elements

Output:
    A list of lists, each representing a different subset of lIIllIIIIlIlI. The empty set is always a subset of lIIllIIIIlIlI, and lIIllIIIIlIlI is always a subset of lIIllIIIIlIlI.

Example:
    >>> IIIlIlIlIIIII(['a', 'b', 'c'])
    [[], ['c'], ['b'], ['b', 'c'], ['a'], ['a', 'c'], ['a', 'b'], ['a', 'b', 'c']]
"""

def IIIlIlIlIIIII(lIIllIIIIlIlI):
    if lIIllIIIIlIlI:
        llIlIlIllllIIIII, *IllIIIIIllIIlIl = lIIllIIIIlIlI 
        IlIIIllIllIl = IIIlIlIlIIIII(IllIIIIIllIIlIl)
        return [[llIlIlIllllIIIII] + IllIIIllIIIlIIl for IllIIIllIIIlIIl in IlIIIllIllIl]
    else:
        return [[]]