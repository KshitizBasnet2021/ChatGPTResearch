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