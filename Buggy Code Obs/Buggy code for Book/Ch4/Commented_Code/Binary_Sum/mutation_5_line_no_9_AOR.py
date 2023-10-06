def lllIIIlIIIlI(IlllIIlIIlIllIIllI, lIlIlIIIllI, IIlllIlIIIIllIl):
  if lIlIlIIIllI >= IIlllIlIIIIllIl:                      
    return 0
  elif lIlIlIIIllI == IIlllIlIIIIllIl-1:                  
    return IlllIIlIIlIllIIllI[lIlIlIIIllI]
  else:                                  
    llIIlIlllIIIlII = (lIlIlIIIllI + IIlllIlIIIIllIl) // 2
    return lllIIIlIIIlI(IlllIIlIIlIllIIllI, lIlIlIIIllI, llIIlIlllIIIlII) - lllIIIlIIIlI(IlllIIlIIlIllIIllI, llIIlIlllIIIlII, IIlllIlIIIIllIl)