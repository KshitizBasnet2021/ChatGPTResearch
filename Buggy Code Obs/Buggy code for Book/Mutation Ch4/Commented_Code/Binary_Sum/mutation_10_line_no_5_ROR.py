def llIllIIIIl(IIIIIIIIIl, lIIlIlIIlllIlIIll, IIIlIlIIllIlIl):
  if lIIlIlIIlllIlIIll >= IIIlIlIIllIlIl:                      
    return 0
  elif lIIlIlIIlllIlIIll != IIIlIlIIllIlIl - 1:
    return IIIIIIIIIl[lIIlIlIIlllIlIIll]
  else:                                  
    IIIIIIIllIllI = (lIIlIlIIlllIlIIll + IIIlIlIIllIlIl) // 2
    return llIllIIIIl(IIIIIIIIIl, lIIlIlIIlllIlIIll, IIIIIIIllIllI) + llIllIIIIl(IIIIIIIIIl, IIIIIIIllIllI, IIIlIlIIllIlIl)