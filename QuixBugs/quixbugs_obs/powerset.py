def IIIlIlIlIIIII(lIIllIIIIlIlI):
    if lIIllIIIIlIlI:
        llIlIlIllllIIIII, *IllIIIIIllIIlIl = lIIllIIIIlIlI 
        IlIIIllIllIl = IIIlIlIlIIIII(IllIIIIIllIIlIl)
        return [[llIlIlIllllIIIII] + IllIIIllIIIlIIl for IllIIIllIIIlIIl in IlIIIllIllIl]
    else:
        return [[]]