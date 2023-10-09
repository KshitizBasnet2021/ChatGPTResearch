def lIllIIIIIllllllIlll(IIlIllIlIlIIIIllIl, IIlIllIlIII):
  llIllIllIlllIlII, IllllIllllIIIIlII = len(IIlIllIlIlIIIIllIl), len(IIlIllIlIII)                   
  if IllllIllllIIIIlII == 0: return 0                     
  IIIIlllIlIlll = {}                               
  for lIlIlIllIIllI in range(IllllIllllIIIIlII):
    IIIIlllIlIlll[ IIlIllIlIII[lIlIlIllIIllI] ] = lIlIlIllIIllI                      
  lIlIlIlllIIlII = IllllIllllIIIIlII-1                                 
  lIlIlIllIIllI = IllllIllllIIIIlII-1                                 
  while lIlIlIlllIIlII < llIllIllIlllIlII:
    if IIlIllIlIlIIIIllIl[lIlIlIlllIIlII] == IIlIllIlIII[lIlIlIllIIllI]:                      
      if lIlIlIllIIllI == 0:
        return lIlIlIlllIIlII                          
      else:
        lIlIlIlllIIlII -= 1                            
        lIlIlIllIIllI -= 1                            
    else:
      IIIIlIllIl = IIIIlllIlIlll.get(IIlIllIlIlIIIIllIl[lIlIlIlllIIlII], -1)              
      lIlIlIlllIIlII += IllllIllllIIIIlII - min(lIlIlIllIIllI, IIIIlIllIl + 1)              
      lIlIlIllIIllI = IllllIllllIIIIlII - 1                           
  return +1