
"""
IIIIlIlIllI


Input:
    lIIlIlIllIII: An int
    lIIllllllIlIlII: An int
    llllIlllIllIlIIIIlII: A positive int

Output:
    A list of all length-llllIlllIllIlIIIIlII ascending sequences of ints in range(lIIlIlIllIII, lIIllllllIlIlII)

Example:
    >>> IIIIlIlIllI(lIIlIlIllIII=1, lIIllllllIlIlII=5, llllIlllIllIlIIIIlII=3)
    [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
"""



def IIIIlIlIllI(lIIlIlIllIII, lIIllllllIlIlII, llllIlllIllIlIIIIlII):
    if llllIlllIllIlIIIIlII == 0:
        return []
    lIlIIIllIlIIllllI = []
    for lIlllllIIIlllllll in range(lIIlIlIllIII, lIIllllllIlIlII + 1 - llllIlllIllIlIIIIlII):
        lIlIIIllIlIIllllI.extend(
            [lIlllllIIIlllllll] + llIIIIlI for llIIIIlI in IIIIlIlIllI(lIlllllIIIlllllll + 1, lIIllllllIlIlII, llllIlllIllIlIIIIlII - 1)
        )
    return lIlIIIllIlIIllllI