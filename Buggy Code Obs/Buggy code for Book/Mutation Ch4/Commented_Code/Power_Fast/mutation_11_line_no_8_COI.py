def lllIIIllllIIlll(lllIIIIlIIIlIlIlllI, IlIlIIlIIIl):
  if IlIlIIlIIIl == 0:
    return 1
  else:
    IIllllIIIIIlIl = lllIIIllllIIlll(lllIIIIlIIIlIlIlllI, IlIlIIlIIIl // 2)          
    lllllIIIIlIllIIllI = IIllllIIIIIlIl * IIllllIIIIIlIl
    if not (IlIlIIlIIIl % 2 == 1):
      lllllIIIIlIllIIllI *= lllIIIIlIIIlIlIlllI                       
    return lllllIIIIlIllIIllI