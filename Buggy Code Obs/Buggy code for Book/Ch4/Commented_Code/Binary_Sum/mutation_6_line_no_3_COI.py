def IllllIIlIIIIIlIlllII(llIllIllllIIllI, lIlllIIllIllIlllI, IlIlIIIlIIIlIIlIIll):
  if not (lIlllIIllIllIlllI >= IlIlIIIlIIIlIIlIIll):
    return 0
  elif lIlllIIllIllIlllI == IlIlIIIlIIIlIIlIIll-1:                  
    return llIllIllllIIllI[lIlllIIllIllIlllI]
  else:                                  
    IIlIIlllIIlIIl = (lIlllIIllIllIlllI + IlIlIIIlIIIlIIlIIll) // 2
    return IllllIIlIIIIIlIlllII(llIllIllllIIllI, lIlllIIllIllIlllI, IIlIIlllIIlIIl) + IllllIIlIIIIIlIlllII(llIllIllllIIllI, IIlIIlllIIlIIl, IlIlIIIlIIIlIIlIIll)