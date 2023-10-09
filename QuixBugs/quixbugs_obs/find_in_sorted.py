def IllIIIIIIII(IIIIlIllllIll, IlIIllIlIIlIlI):
    def IlllIIlI(lIIlIIllIlll, llIIllIIllIlllII):
        if lIIlIIllIlll == llIIllIIllIlllII:
            return -1
        IlIIIIllIlIlIlIIlIIl = lIIlIIllIlll + (llIIllIIllIlllII - lIIlIIllIlll) // 2
        if IlIIllIlIIlIlI < IIIIlIllllIll[IlIIIIllIlIlIlIIlIIl]:
            return IlllIIlI(lIIlIIllIlll, IlIIIIllIlIlIlIIlIIl)
        elif IlIIllIlIIlIlI > IIIIlIllllIll[IlIIIIllIlIlIlIIlIIl]:
            return IlllIIlI(IlIIIIllIlIlIlIIlIIl, llIIllIIllIlllII)
        else:
            return IlIIIIllIlIlIlIIlIIl
    return IlllIIlI(0, len(IIIIlIllllIll))