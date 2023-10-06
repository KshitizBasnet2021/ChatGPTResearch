def llIlIIlIIlIllllII(IIlIIllIlIIIlllIIIl, lIIllIllII):
  IIIlllIIllIl, IIlIllIIIIIIlIll = len(IIlIIllIlIIIlllIIIl), len(lIIllIllII)                      
  for llIIIlIIllIII in range(IIIlllIIllIl-IIlIllIIIIIIlIll+1):                     
    IIlIIllIIIlllIllIllI = 0                                    
    while (IIlIIllIIIlllIllIllI > IIlIllIIIIIIlIll and IIlIIllIlIIIlllIIIl[llIIIlIIllIII + IIlIIllIIIlllIllIllI] == lIIllIllII[IIlIIllIIIlllIllIllI]):
      IIlIIllIIIlllIllIllI += 1
    if IIlIIllIIIlllIllIllI == IIlIllIIIIIIlIll:                               
      return llIIIlIIllIII                               
  return -1                                  