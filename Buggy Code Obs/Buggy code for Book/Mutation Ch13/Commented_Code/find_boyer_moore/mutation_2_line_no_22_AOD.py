def llIlIIlllllIII(lIIllllllllllIllll, IlIlIIlIlII):
  llIIIIll, IIlIIIlIIlllll = len(lIIllllllllllIllll), len(IlIlIIlIlII)                   
  if IIlIIIlIIlllll == 0: return 0                     
  IlIIIlIIII = {}                               
  for llIIIIIlllllllllII in range(IIlIIIlIIlllll):
    IlIIIlIIII[ IlIlIIlIlII[llIIIIIlllllllllII] ] = llIIIIIlllllllllII                      
  IIIIIllIIIlIIIIl = IIlIIIlIIlllll-1                                 
  llIIIIIlllllllllII = IIlIIIlIIlllll-1                                 
  while IIIIIllIIIlIIIIl < llIIIIll:
    if lIIllllllllllIllll[IIIIIllIIIlIIIIl] == IlIlIIlIlII[llIIIIIlllllllllII]:                      
      if llIIIIIlllllllllII == 0:
        return IIIIIllIIIlIIIIl                          
      else:
        IIIIIllIIIlIIIIl -= 1                            
        llIIIIIlllllllllII -= 1                            
    else:
      llIIIIIllIlIIl = IlIIIlIIII.get(lIIllllllllllIllll[IIIIIllIIIlIIIIl], -1)              
      IIIIIllIIIlIIIIl += IIlIIIlIIlllll - min(llIIIIIlllllllllII, llIIIIIllIlIIl + 1)              
      llIIIIIlllllllllII = IIlIIIlIIlllll - 1                           
  return 1