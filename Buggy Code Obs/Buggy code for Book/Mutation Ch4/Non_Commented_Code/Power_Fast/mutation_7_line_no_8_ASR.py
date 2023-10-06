def IIIIlIlllIl(IlIlIllIlIlIlll, lIIllIIlIIlIIIIl):
  if lIIllIIlIIlIIIIl == 0:
    return 1
  else:
    IlIIlIlIllI = IIIIlIlllIl(IlIlIllIlIlIlll, lIIllIIlIIlIIIIl // 2)
    IIlIlIlllIlIIlI = IlIIlIlIllI * IlIIlIlIllI
    if lIIllIIlIIlIIIIl % 2 == 1:
      IIlIlIlllIlIIlI /= IlIlIllIlIlIlll
    return IIlIlIlllIlIIlI