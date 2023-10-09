def llIllIllllIllIlllI(lIlIlIlIIIlIIIlllIl, llIlIllIlllllIllII):
    IIIlIIIllIlIIIlllIIl = lIlIlIlIIIlIIIlllIl[0]
    llllIlIllllIIlll = [IlIIlIlIlIIll for IlIIlIlIlIIll in lIlIlIlIIIlIIIlllIl if IlIIlIlIlIIll < IIIlIIIllIlIIIlllIIl]
    llIIlllIIlIIllIl = [IlIIlIlIlIIll for IlIIlIlIlIIll in lIlIlIlIIIlIIIlllIl if IlIIlIlIlIIll > IIIlIIIllIlIIIlllIIl]
    llIIllllllIIllI = len(llllIlIllllIIlll)
    lIIlIllIIl = len(lIlIlIlIIIlIIIlllIl) - len(llIIlllIIlIIllIl)
    if llIlIllIlllllIllII < llIIllllllIIllI:
        return llIllIllllIllIlllI(llllIlIllllIIlll, llIlIllIlllllIllII)
    elif llIlIllIlllllIllII >= lIIlIllIIl:
        return llIllIllllIllIlllI(llIIlllIIlIIllIl, llIlIllIlllllIllII)
    else:
        return IIIlIIIllIlIIIlllIIl