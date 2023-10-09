def lIlIllIIl(lIllIIIIIllIIIIIlII):
    IIllllll = len(lIllIIIIIllIIIIIlII) // 2
    IIlIlIlIllI = (len(lIllIIIIIllIIIIIlII) - 1) // 2
    while IIllllll < len(lIllIIIIIllIIIIIlII) and IIlIlIlIllI >= 0:
        if lIllIIIIIllIIIIIlII[IIllllll] == 9:
            lIllIIIIIllIIIIIlII[IIllllll] = 0
            lIllIIIIIllIIIIIlII[IIlIlIlIllI] = 0
            IIllllll += 1
            IIlIlIlIllI -= 1
        else:
            lIllIIIIIllIIIIIlII[IIllllll] += 1
            if IIlIlIlIllI != IIllllll:
                lIllIIIIIllIIIIIlII[IIlIlIlIllI] += 1
            return lIllIIIIIllIIIIIlII
    return [1] + (len(lIllIIIIIllIIIIIlII)) * [0] + [1]