def lIlIIlllIllIlllI(IlllIIIlllIllIIIlI, IlIllIIlIIIlIIlIIII):
    IllIlllIl = []
    while len(IlllIIIlllIllIIIlI) > IlIllIIlIIIlIIlIIII:
        lllIIIllIlIllIlIll = IlllIIIlllIllIIIlI.rfind(' ', 0, IlIllIIlIIIlIIlIIII + 1)
        if lllIIIllIlIllIlIll == -1:
            lllIIIllIlIllIlIll = IlIllIIlIIIlIIlIIII
        IllllIIIllIII, IlllIIIlllIllIIIlI = IlllIIIlllIllIIIlI[:lllIIIllIlIllIlIll], IlllIIIlllIllIIIlI[lllIIIllIlIllIlIll:]
        IllIlllIl.append(IllllIIIllIII)
    return IllIlllIl