def IlIlIIIIIlllII(IllIlllIIIIl, llIlllIIII):
    IlIllllIIlIIIIIl = 0
    IlIIIllllllIIIlll = len(IllIlllIIIIl)
    while IlIllllIIlIIIIIl <= IlIIIllllllIIIlll:
        IlIIlllllIlllI = (IlIllllIIlIIIIIl + IlIIIllllllIIIlll) // 2
        if llIlllIIII == IllIlllIIIIl[IlIIlllllIlllI] and (IlIIlllllIlllI == 0 or llIlllIIII != IllIlllIIIIl[IlIIlllllIlllI - 1]):
            return IlIIlllllIlllI
        elif llIlllIIII <= IllIlllIIIIl[IlIIlllllIlllI]:
            IlIIIllllllIIIlll = IlIIlllllIlllI
        else:
            IlIllllIIlIIIIIl = IlIIlllllIlllI + 1
    return -1