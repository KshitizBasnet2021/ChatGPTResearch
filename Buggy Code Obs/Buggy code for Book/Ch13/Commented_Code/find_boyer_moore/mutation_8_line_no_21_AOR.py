def llIIIllllI(llIlIlIllIIIIIII, IlIIIllII):
  IlIlllIlIlII, IlllllIIIlIllIllIlI = len(llIlIlIllIIIIIII), len(IlIIIllII)                   
  if IlllllIIIlIllIllIlI == 0: return 0                     
  lIllllllIIllIIlIII = {}                               
  for lIlIIIlIll in range(IlllllIIIlIllIllIlI):
    lIllllllIIllIIlIII[ IlIIIllII[lIlIIIlIll] ] = lIlIIIlIll                      
  IlIIlllIIllIIlIll = IlllllIIIlIllIllIlI-1                                 
  lIlIIIlIll = IlllllIIIlIllIllIlI-1                                 
  while IlIIlllIIllIIlIll < IlIlllIlIlII:
    if llIlIlIllIIIIIII[IlIIlllIIllIIlIll] == IlIIIllII[lIlIIIlIll]:                      
      if lIlIIIlIll == 0:
        return IlIIlllIIllIIlIll                          
      else:
        IlIIlllIIllIIlIll -= 1                            
        lIlIIIlIll -= 1                            
    else:
      lllIIIlIII = lIllllllIIllIIlIII.get(llIlIlIllIIIIIII[IlIIlllIIllIIlIll], -1)              
      IlIIlllIIllIIlIll += IlllllIIIlIllIllIlI - min(lIlIIIlIll, lllIIIlIII + 1)              
      lIlIIIlIll = IlllllIIIlIllIllIlI + 1
  return -1