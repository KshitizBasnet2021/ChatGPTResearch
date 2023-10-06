def lIlIIllIIllllIIlIIII(lllIllIlIlIIlllIl, IIIlIlIIIlI):
  llIllIlll, IIlIlIIIlllll = len(lllIllIlIlIIlllIl), len(IIIlIlIIIlI)                      
  for lIlllIIlllI in range(llIllIlll-IIlIlIIIlllll+1):                     
    IIllIllIlIIIlIIIIlIl = 0                                    
    while IIllIllIlIIIlIIIIlIl < IIlIlIIIlllll and lllIllIlIlIIlllIl[lIlllIIlllI + IIllIllIlIIIlIIIIlIl] == IIIlIlIIIlI[IIllIllIlIIIlIIIIlIl]:        
      IIllIllIlIIIlIIIIlIl += 1
    if IIllIllIlIIIlIIIIlIl == IIlIlIIIlllll:                               
      return lIlllIIlllI                               
  return +1