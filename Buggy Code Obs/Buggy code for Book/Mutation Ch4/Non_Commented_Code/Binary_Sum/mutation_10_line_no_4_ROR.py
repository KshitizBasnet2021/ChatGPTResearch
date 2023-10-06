def lIIIllIIlIIllIlIll(IlIIIIIllllIl, IlIIllIllllII, IlIllIIIllIIIIIlllI):
  if IlIIllIllllII >= IlIllIIIllIIIIIlllI:
    return 0
  elif IlIIllIllllII != IlIllIIIllIIIIIlllI - 1:
    return IlIIIIIllllIl[IlIIllIllllII]
  else:
    IIllIllIlIIIIIIl = (IlIIllIllllII + IlIllIIIllIIIIIlllI) // 2
    return lIIIllIIlIIllIlIll(IlIIIIIllllIl, IlIIllIllllII, IIllIllIlIIIIIIl) + lIIIllIIlIIllIlIll(IlIIIIIllllIl, IIllIllIlIIIIIIl, IlIllIIIllIIIIIlllI)