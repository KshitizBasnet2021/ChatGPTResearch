def IIllIllllIIIl(llIlIIIlIlII, IlIIIIlllllIlIlllIIl, IIlIIIllIIIlllI):
  if IlIIIIlllllIlIlllIIl >= IIlIIIllIIIlllI:                      
    return 0
  elif IlIIIIlllllIlIlllIIl == IIlIIIllIIIlllI-1:                  
    return llIlIIIlIlII[IlIIIIlllllIlIlllIIl]
  else:                                  
    IllIlIlll = (IlIIIIlllllIlIlllIIl + IIlIIIllIIIlllI) / 2
    return IIllIllllIIIl(llIlIIIlIlII, IlIIIIlllllIlIlllIIl, IllIlIlll) + IIllIllllIIIl(llIlIIIlIlII, IllIlIlll, IIlIIIllIIIlllI)