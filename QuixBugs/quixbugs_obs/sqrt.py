def IlIllllIlI(lIIIIIlIIIlll, IlIIlIII):
    llllIIllIIIIlIl = lIIIIIlIIIlll / 2
    while abs(lIIIIIlIIIlll - llllIIllIIIIlIl) > IlIIlIII:
        llllIIllIIIIlIl = 0.5 * (llllIIllIIIIlIl + lIIIIIlIIIlll / llllIIllIIIIlIl)
    return llllIIllIIIIlIl