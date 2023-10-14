
"""
IlllIlIIlIll


Input:
    IlIIlIIlllIlllIll: A list of ints

Output:
    The elements of IlIIlIIlllIlllIll in sorted order
"""

def IlllIlIIlIll(IlIIlIIlllIlllIll):
    if not IlIIlIIlllIlllIll:
        return []
    IIIlIllIlIIlIlIlll = IlIIlIIlllIlllIll[0]
    lllIlIIIl = IlllIlIIlIll([lllIllIIl for lllIllIIl in IlIIlIIlllIlllIll[1:] if lllIllIIl < IIIlIllIlIIlIlIlll])
    lllIIllIIIl = IlllIlIIlIll([lllIllIIl for lllIllIIl in IlIIlIIlllIlllIll[1:] if lllIllIIl > IIIlIllIlIIlIlIlll])
    return lllIlIIIl + [IIIlIllIlIIlIlIlll] + lllIIllIIIl