def IllllllIlIIIlIlIIllI(IIllIIIlIIlIIlIIl, IIIlIIlllIlIllIlII):
  llIlIIlIllIlIIll, lIlIlIIllIllllIl = len(IIllIIIlIIlIIlIIl), len(IIIlIIlllIlIllIlII)                   
  if lIlIlIIllIllllIl == 0: return 0                     
  lllIIIlllIl = {}                               
  for IIIIIlll in range(lIlIlIIllIllllIl):
    lllIIIlllIl[ IIIlIIlllIlIllIlII[IIIIIlll] ] = IIIIIlll                      
  lllIIlIlllI = lIlIlIIllIllllIl-1                                 
  IIIIIlll = lIlIlIIllIllllIl-1                                 
  while lllIIlIlllI <= llIlIIlIllIlIIll:
    if IIllIIIlIIlIIlIIl[lllIIlIlllI] == IIIlIIlllIlIllIlII[IIIIIlll]:                      
      if IIIIIlll == 0:
        return lllIIlIlllI                          
      else:
        lllIIlIlllI -= 1                            
        IIIIIlll -= 1                            
    else:
      lIlIIllI = lllIIIlllIl.get(IIllIIIlIIlIIlIIl[lllIIlIlllI], -1)              
      lllIIlIlllI += lIlIlIIllIllllIl - min(IIIIIlll, lIlIIllI + 1)              
      IIIIIlll = lIlIlIIllIllllIl - 1                           
  return -1