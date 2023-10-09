def lllIIIlIllIllII(llIIIIllIIlIlII, IlIlIllllIIlII):
  IIlIlIllIlIlIII, lllllllIII = len(llIIIIllIIlIlII), len(IlIlIllllIIlII)                   
  if lllllllIII == 0: return 0                     
  lllIlllIIlllllIl = {}                               
  for IIlllIIIl in range(lllllllIII):
    lllIlllIIlllllIl[ IlIlIllllIIlII[IIlllIIIl] ] = IIlllIIIl                      
  llllIIlIllIl = lllllllIII-1                                 
  IIlllIIIl = lllllllIII-1                                 
  while llllIIlIllIl < IIlIlIllIlIlIII:
    if not (llIIIIllIIlIlII[llllIIlIllIl] == IlIlIllllIIlII[IIlllIIIl]):
      if IIlllIIIl == 0:
        return llllIIlIllIl                          
      else:
        llllIIlIllIl -= 1                            
        IIlllIIIl -= 1                            
    else:
      IlIIIIIlllIllII = lllIlllIIlllllIl.get(llIIIIllIIlIlII[llllIIlIllIl], -1)              
      llllIIlIllIl += lllllllIII - min(IIlllIIIl, IlIIIIIlllIllII + 1)              
      IIlllIIIl = lllllllIII - 1                           
  return -1