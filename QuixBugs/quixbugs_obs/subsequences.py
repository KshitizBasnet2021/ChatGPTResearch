def IIIIlIlIllI(lIIlIlIllIII, lIIllllllIlIlII, llllIlllIllIlIIIIlII):
    if llllIlllIllIlIIIIlII == 0:
        return []
    lIlIIIllIlIIllllI = []
    for lIlllllIIIlllllll in range(lIIlIlIllIII, lIIllllllIlIlII + 1 - llllIlllIllIlIIIIlII):
        lIlIIIllIlIIllllI.extend(
            [lIlllllIIIlllllll] + llIIIIlI for llIIIIlI in IIIIlIlIllI(lIlllllIIIlllllll + 1, lIIllllllIlIlII, llllIlllIllIlIIIIlII - 1)
        )
    return lIlIIIllIlIIllllI