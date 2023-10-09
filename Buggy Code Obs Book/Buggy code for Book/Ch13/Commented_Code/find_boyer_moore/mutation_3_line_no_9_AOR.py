def llIIIIlllIIlIIlIII(llIIlIlllIlIl, llIIIIlIlIllIllIIlIl):
  lIlIIIlII, IIlIlIIII = len(llIIlIlllIlIl), len(llIIIIlIlIllIllIIlIl)                   
  if IIlIlIIII == 0: return 0                     
  IlllIlIllIl = {}                               
  for IIllIIll in range(IIlIlIIII):
    IlllIlIllIl[ llIIIIlIlIllIllIIlIl[IIllIIll] ] = IIllIIll                      
  llIIIIlllIIIlIllIlll = IIlIlIIII + 1
  IIllIIll = IIlIlIIII-1                                 
  while llIIIIlllIIIlIllIlll < lIlIIIlII:
    if llIIlIlllIlIl[llIIIIlllIIIlIllIlll] == llIIIIlIlIllIllIIlIl[IIllIIll]:                      
      if IIllIIll == 0:
        return llIIIIlllIIIlIllIlll                          
      else:
        llIIIIlllIIIlIllIlll -= 1                            
        IIllIIll -= 1                            
    else:
      lIlllIllI = IlllIlIllIl.get(llIIlIlllIlIl[llIIIIlllIIIlIllIlll], -1)              
      llIIIIlllIIIlIllIlll += IIlIlIIII - min(IIllIIll, lIlllIllI + 1)              
      IIllIIll = IIlIlIIII - 1                           
  return -1