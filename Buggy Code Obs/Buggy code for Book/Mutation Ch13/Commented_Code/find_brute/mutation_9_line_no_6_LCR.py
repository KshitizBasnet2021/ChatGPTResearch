def IIllllIIlIII(lIlIlIllIIIIII, IlIllllIIlIlII):
  IllIIIIlIl, IllllIIlIIIIl = len(lIlIlIllIIIIII), len(IlIllllIIlIlII)                      
  for IIlIllIIIIIllIIIl in range(IllIIIIlIl-IllllIIlIIIIl+1):                     
    IlllIIIIIllIlIIIll = 0                                    
    while (IlllIIIIIllIlIIIll < IllllIIlIIIIl or lIlIlIllIIIIII[IIlIllIIIIIllIIIl + IlllIIIIIllIlIIIll] == IlIllllIIlIlII[IlllIIIIIllIlIIIll]):
      IlllIIIIIllIlIIIll += 1
    if IlllIIIIIllIlIIIll == IllllIIlIIIIl:                               
      return IIlIllIIIIIllIIIl                               
  return -1                                  