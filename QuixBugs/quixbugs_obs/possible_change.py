def IllllIllIIllIlIIllll(lIlIIIlIllIlIIl, llIlIIIIIlIlllIII):
    if llIlIIIIIlIlllIII == 0:
        return 1
    if llIlIIIIIlIlllIII < 0:
        return 0
    lIIlIIlIIII, *IIIIlllIIlIII = lIlIIIlIllIlIIl
    return IllllIllIIllIlIIllll(lIlIIIlIllIlIIl, llIlIIIIIlIlllIII - lIIlIIlIIII) + IllllIllIIllIlIIllll(IIIIlllIIlIII, llIlIIIIIlIlllIII)