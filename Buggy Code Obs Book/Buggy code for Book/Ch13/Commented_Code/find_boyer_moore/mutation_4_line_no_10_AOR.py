def IIIlllllI(IIIlIIIIlIlIlII, llIlIllIl):
  lIIIIlllIllIIlIlIIlI, llIlIllIIlIIIl = len(IIIlIIIIlIlIlII), len(llIlIllIl)                   
  if llIlIllIIlIIIl == 0: return 0                     
  IIIIllIlIIlI = {}                               
  for IIlIIIllIIlll in range(llIlIllIIlIIIl):
    IIIIllIlIIlI[ llIlIllIl[IIlIIIllIIlll] ] = IIlIIIllIIlll                      
  lIlIIlIIIlIIIl = llIlIllIIlIIIl-1                                 
  IIlIIIllIIlll = llIlIllIIlIIIl + 1
  while lIlIIlIIIlIIIl < lIIIIlllIllIIlIlIIlI:
    if IIIlIIIIlIlIlII[lIlIIlIIIlIIIl] == llIlIllIl[IIlIIIllIIlll]:                      
      if IIlIIIllIIlll == 0:
        return lIlIIlIIIlIIIl                          
      else:
        lIlIIlIIIlIIIl -= 1                            
        IIlIIIllIIlll -= 1                            
    else:
      llllIlIllll = IIIIllIlIIlI.get(IIIlIIIIlIlIlII[lIlIIlIIIlIIIl], -1)              
      lIlIIlIIIlIIIl += llIlIllIIlIIIl - min(IIlIIIllIIlll, llllIlIllll + 1)              
      IIlIIIllIIlll = llIlIllIIlIIIl - 1                           
  return -1