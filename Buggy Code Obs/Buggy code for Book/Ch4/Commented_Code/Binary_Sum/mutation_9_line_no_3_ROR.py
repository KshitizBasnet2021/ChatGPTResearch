def IllIlIlllIIl(llIlIIlIIIIlIlllII, IIllllIIIl, lIIllIIllIIllIlIlII):
  if IIllllIIIl > lIIllIIllIIllIlIlII:
    return 0
  elif IIllllIIIl == lIIllIIllIIllIlIlII-1:                  
    return llIlIIlIIIIlIlllII[IIllllIIIl]
  else:                                  
    lIIIIIIlIIlllIIII = (IIllllIIIl + lIIllIIllIIllIlIlII) // 2
    return IllIlIlllIIl(llIlIIlIIIIlIlllII, IIllllIIIl, lIIIIIIlIIlllIIII) + IllIlIlllIIl(llIlIIlIIIIlIlllII, lIIIIIIlIIlllIIII, lIIllIIllIIllIlIlII)