def llIlIIIIllIlIIIllI(IlIllIlIIIlIIIIIIIIl, IIIllIllllIlIIlIlIl):
    llIllIII = [0] * IIIllIllllIlIIlIlIl
    for IIIlIIllIIlIlll in IlIllIlIIIlIIIIIIIIl:
        llIllIII[IIIlIIllIIlIlll] += 1
    lIlIlIlIllIIIllIII = []
    for IlllIIllllIllIIlll, IIlIlllllIIIlI in enumerate(IlIllIlIIIlIIIIIIIIl):
        lIlIlIlIllIIIllIII.extend([IlllIIllllIllIIlll] * IIlIlllllIIIlI)
    return lIlIlIlIllIIIllIII