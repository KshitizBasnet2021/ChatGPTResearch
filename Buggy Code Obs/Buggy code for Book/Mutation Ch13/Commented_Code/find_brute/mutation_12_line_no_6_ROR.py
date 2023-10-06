def IlllllIIlllllllIIIl(IIlIIllIIlI, lllIlllllIllI):
  IIIIIIIIIl, lIlIIlIlII = len(IIlIIllIIlI), len(lllIlllllIllI)                      
  for lIlllIIIlllIlll in range(IIIIIIIIIl-lIlIIlIlII+1):                     
    IIlIIIlII = 0                                    
    while (IIlIIIlII < lIlIIlIlII and IIlIIllIIlI[lIlllIIIlllIlll + IIlIIIlII] != lllIlllllIllI[IIlIIIlII]):
      IIlIIIlII += 1
    if IIlIIIlII == lIlIIlIlII:                               
      return lIlllIIIlllIlll                               
  return -1                                  