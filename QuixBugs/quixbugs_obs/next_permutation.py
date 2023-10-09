def llllllIIIl(IlIlIIIlIIl):
    for IIIlIlIlI in range(len(IlIlIIIlIIl) - 2, -1, -1):
        if IlIlIIIlIIl[IIIlIlIlI] < IlIlIIIlIIl[IIIlIlIlI + 1]:
            for lIlIIIIlIIlIIIIlII in range(len(IlIlIIIlIIl) - 1, IIIlIlIlI, -1):
                if IlIlIIIlIIl[lIlIIIIlIIlIIIIlII] < IlIlIIIlIIl[IIIlIlIlI]:
                    IIllIllIIIlI = list(IlIlIIIlIIl)
                    IIllIllIIIlI[IIIlIlIlI], IIllIllIIIlI[lIlIIIIlIIlIIIIlII] = IlIlIIIlIIl[lIlIIIIlIIlIIIIlII], IlIlIIIlIIl[IIIlIlIlI]
                    IIllIllIIIlI[IIIlIlIlI + 1:] = reversed(IIllIllIIIlI[IIIlIlIlI + 1:])
                    return IIllIllIIIlI