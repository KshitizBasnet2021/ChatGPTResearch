def IllllIIllllIllIIll(IIlIllIllIlIlII, IlIIllIllIIIlIllI):
  if IlIIllIllIIIlIllI == 0:
    return 1
  else:
    llIlIlIIIlIIIl = IllllIIllllIllIIll(IIlIllIllIlIlII, IlIIllIllIIIlIllI // 2)
    lllllIIIl = llIlIlIIIlIIIl * llIlIlIIIlIIIl
    if IlIIllIllIIIlIllI * 2 == 1:
      lllllIIIl *= IIlIllIllIlIlII                       
    return lllllIIIl