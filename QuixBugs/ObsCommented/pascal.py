
"""
lIlIIIIIlIIllI



Input:
    lIlIlIIllIllIIlI: The number of rows to return

Precondition:
    lIlIlIIllIllIIlI >= 1

Output:
    The first lIlIlIIllIllIIlI rows of Pascal's triangle as a list of lIlIlIIllIllIIlI lists

Example:
    >>> lIlIIIIIlIIllI(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
"""

def lIlIIIIIlIIllI(lIlIlIIllIllIIlI):
    IIIllIIlIIlII = [[1]]
    for IIIlIIIIIIIlIIlI in range(1, lIlIlIIllIllIIlI):
        lIlIIIIIlIllllIlIl = []
        for IlllllIllI in range(0, IIIlIIIIIIIlIIlI):
            IIllIIllI = IIIllIIlIIlII[IIIlIIIIIIIlIIlI - 1][IlllllIllI - 1] if IlllllIllI > 0 else 0
            lIllIlIllIIIlIllI = IIIllIIlIIlII[IIIlIIIIIIIlIIlI - 1][IlllllIllI] if IlllllIllI < IIIlIIIIIIIlIIlI else 0
            lIlIIIIIlIllllIlIl.append(IIllIIllI + lIllIlIllIIIlIllI)
        IIIllIIlIIlII.append(lIlIIIIIlIllllIlIl)
    return IIIllIIlIIlII