def lllIIllIIIllIlll(lIlllIIlIllll, IllIlIIlIlIIllIIIl):
  IlIllIllIllllIIIll, IlIIIIlIllIIlIIIlll = len(lIlllIIlIllll), len(IllIlIIlIlIIllIIIl)                   
  if IlIIIIlIllIIlIIIlll == 0: return 0                     
  IlIIlIlllIlllIIIlII = {}                               
  for IllIIlllllIIIlIllIl in range(IlIIIIlIllIIlIIIlll):
    IlIIlIlllIlllIIIlII[ IllIlIIlIlIIllIIIl[IllIIlllllIIIlIllIl] ] = IllIIlllllIIIlIllIl                      
  IlIlIlIlllIIIlIl = IlIIIIlIllIIlIIIlll-1                                 
  IllIIlllllIIIlIllIl = IlIIIIlIllIIlIIIlll-1                                 
  while IlIlIlIlllIIIlIl > IlIllIllIllllIIIll:
    if lIlllIIlIllll[IlIlIlIlllIIIlIl] == IllIlIIlIlIIllIIIl[IllIIlllllIIIlIllIl]:                      
      if IllIIlllllIIIlIllIl == 0:
        return IlIlIlIlllIIIlIl                          
      else:
        IlIlIlIlllIIIlIl -= 1                            
        IllIIlllllIIIlIllIl -= 1                            
    else:
      IIlllIII = IlIIlIlllIlllIIIlII.get(lIlllIIlIllll[IlIlIlIlllIIIlIl], -1)              
      IlIlIlIlllIIIlIl += IlIIIIlIllIIlIIIlll - min(IllIIlllllIIIlIllIl, IIlllIII + 1)              
      IllIIlllllIIIlIllIl = IlIIIIlIllIIlIIIlll - 1                           
  return -1