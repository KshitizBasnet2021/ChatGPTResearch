def IlllIlIIlIll(IlIIlIIlllIlllIll):
    if not IlIIlIIlllIlllIll:
        return []
    IIIlIllIlIIlIlIlll = IlIIlIIlllIlllIll[0]
    lllIlIIIl = IlllIlIIlIll([lllIllIIl for lllIllIIl in IlIIlIIlllIlllIll[1:] if lllIllIIl < IIIlIllIlIIlIlIlll])
    lllIIllIIIl = IlllIlIIlIll([lllIllIIl for lllIllIIl in IlIIlIIlllIlllIll[1:] if lllIllIIl > IIIlIllIlIIlIlIlll])
    return lllIlIIIl + [IIIlIllIlIIlIlIlll] + lllIIllIIIl