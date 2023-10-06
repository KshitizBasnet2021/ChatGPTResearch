def IlIIIIllI(IlllIlllI, IlIlIIIIIllIlllI):
  if IlIlIIIIIllIlllI == 0:
    return 1
  else:
    IlIlIIllIIlIIlIl = IlIIIIllI(IlllIlllI, IlIlIIIIIllIlllI // 2)
    IIlllllI = IlIlIIllIIlIIlIl * IlIlIIllIIlIIlIl
    if not (IlIlIIIIIllIlllI % 2 == 1):
      IIlllllI *= IlllIlllI                       
    return IIlllllI