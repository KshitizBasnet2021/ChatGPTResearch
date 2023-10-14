
"""
llIlIIIIllIlIIIllI


Input:
    IlIllIlIIIlIIIIIIIIl: A list of small ints
    IIIllIllllIlIIlIlIl: Upper bound of the size of the ints in IlIllIlIIIlIIIIIIIIl (not inclusive)

Precondition:
    all(isinstance(x, int) and 0 <= x < IIIllIllllIlIIlIlIl for x in IlIllIlIIIlIIIIIIIIl)

Output:
    The elements of IlIllIlIIIlIIIIIIIIl in sorted order
"""

def llIlIIIIllIlIIIllI(IlIllIlIIIlIIIIIIIIl, IIIllIllllIlIIlIlIl):
    llIllIII = [0] * IIIllIllllIlIIlIlIl
    for IIIlIIllIIlIlll in IlIllIlIIIlIIIIIIIIl:
        llIllIII[IIIlIIllIIlIlll] += 1
    lIlIlIlIllIIIllIII = []
    for IlllIIllllIllIIlll, IIlIlllllIIIlI in enumerate(IlIllIlIIIlIIIIIIIIl):
        lIlIlIlIllIIIllIII.extend([IlllIIllllIllIIlll] * IIlIlllllIIIlI)
    return lIlIlIlIllIIIllIII