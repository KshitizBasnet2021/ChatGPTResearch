def IIIlIllI(lIllIIIlll, IllIllII):
    llllIllIlIIIlllIl = {
        IIlIlIlIIll: float('inf') for IIllIllIlIlIIllIlI, IIlIlIlIIll in IllIllII
    }
    llllIllIlIIIlllIl[lIllIIIlll] = 0
    for IIllIllIllIlIII in range(len(llllIllIlIIIlllIl) - 1):
        for (IIllIllIlIlIIllIlI, IIlIlIlIIll), llIIIIIIllIlIIll in IllIllII.items():
            IllIllII[IIllIllIlIlIIllIlI, IIlIlIlIIll] = min(
                llllIllIlIIIlllIl[IIllIllIlIlIIllIlI] + llIIIIIIllIlIIll,
                llllIllIlIIIlllIl[IIlIlIlIIll]
            )
    return llllIllIlIIIlllIl