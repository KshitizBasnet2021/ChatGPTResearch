def llIIIIIIlllllIIl(lIlIIIIIlI, IlIlIIIIIIIlIIlI, lIllllIllIlIlIlIlll):
  if IlIlIIIIIIIlIIlI > lIllllIllIlIlIlIlll - 1:
    lIlIIIIIlI[IlIlIIIIIIIlIIlI], lIlIIIIIlI[lIllllIllIlIlIlIlll-1] = lIlIIIIIlI[lIllllIllIlIlIlIlll-1], lIlIIIIIlI[IlIlIIIIIIIlIIlI]
    llIIIIIIlllllIIl(lIlIIIIIlI, IlIlIIIIIIIlIIlI+1, lIllllIllIlIlIlIlll-1)