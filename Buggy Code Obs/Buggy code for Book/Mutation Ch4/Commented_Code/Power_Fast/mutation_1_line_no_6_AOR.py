def lIlllIlIIIIIllll(lllIllIlllIIIl, IIlIIIIIllllI):
  if IIlIIIIIllllI == 0:
    return 1
  else:
    IllIIIlIlllII = lIlllIlIIIIIllll(lllIllIlllIIIl, IIlIIIIIllllI / 2)
    lllllIIllll = IllIIIlIlllII * IllIIIlIlllII
    if IIlIIIIIllllI % 2 == 1:                      
      lllllIIllll *= lllIllIlllIIIl                       
    return lllllIIllll