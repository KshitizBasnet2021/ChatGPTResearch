def IllllIll(lIllllIll):
    lIllllIlIIII = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    lIlIlIlIIlIlIlIIllI = []
    lIIlllIllIlllIlIIlII = []
    for IlllIlIIl in lIllllIll:
        if isinstance(IlllIlIIl, int):
            lIlIlIlIIlIlIlIIllI.append(IlllIlIIl)
        else:
            while lIIlllIllIlllIlIIlII and lIllllIlIIII[IlllIlIIl] <= lIllllIlIIII[lIIlllIllIlllIlIIlII[-1]]:
                lIlIlIlIIlIlIlIIllI.append(lIIlllIllIlllIlIIlII.pop())
    while lIIlllIllIlllIlIIlII:
        lIlIlIlIIlIlIlIIllI.append(lIIlllIllIlllIlIIlII.pop())
    return lIlIlIlIIlIlIlIIllI