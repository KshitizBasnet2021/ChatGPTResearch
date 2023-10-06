def IIIIlIIIlllIII(lIIlIlIIllIIllI, IIIlllIllIlII):
  llIIIIIIlIlIllIlIIl, lIIIllIIl = len(lIIlIlIIllIIllI), len(IIIlllIllIlII)                      
  for lIIlIlIIlllIllIlllI in range(llIIIIIIlIlIllIlIIl-lIIIllIIl+1):                     
    lIIIIllIIlIll = 0                                    
    while (lIIIIllIIlIll <= lIIIllIIl and lIIlIlIIllIIllI[lIIlIlIIlllIllIlllI + lIIIIllIIlIll] == IIIlllIllIlII[lIIIIllIIlIll]):
      lIIIIllIIlIll += 1
    if lIIIIllIIlIll == lIIIllIIl:                               
      return lIIlIlIIlllIllIlllI                               
  return -1                                  