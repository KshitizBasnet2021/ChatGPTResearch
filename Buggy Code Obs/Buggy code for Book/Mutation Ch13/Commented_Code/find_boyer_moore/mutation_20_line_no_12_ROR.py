def lllllIlIIl(lIIIllIllIIlIIllIlll, llllIlIlIlIllI):
  IIIlIIlIlIlllIllI, llIllIlllllIIlIl = len(lIIIllIllIIlIIllIlll), len(llllIlIlIlIllI)                   
  if llIllIlllllIIlIl == 0: return 0                     
  lIIIlIllllIlllll = {}                               
  for IIlllllIIlIIlII in range(llIllIlllllIIlIl):
    lIIIlIllllIlllll[ llllIlIlIlIllI[IIlllllIIlIIlII] ] = IIlllllIIlIIlII                      
  IllIIIIllllll = llIllIlllllIIlIl-1                                 
  IIlllllIIlIIlII = llIllIlllllIIlIl-1                                 
  while IllIIIIllllll < IIIlIIlIlIlllIllI:
    if lIIIllIllIIlIIllIlll[IllIIIIllllll] != llllIlIlIlIllI[IIlllllIIlIIlII]:
      if IIlllllIIlIIlII == 0:
        return IllIIIIllllll                          
      else:
        IllIIIIllllll -= 1                            
        IIlllllIIlIIlII -= 1                            
    else:
      lIIlIIllIllllIl = lIIIlIllllIlllll.get(lIIIllIllIIlIIllIlll[IllIIIIllllll], -1)              
      IllIIIIllllll += llIllIlllllIIlIl - min(IIlllllIIlIIlII, lIIlIIllIllllIl + 1)              
      IIlllllIIlIIlII = llIllIlllllIIlIl - 1                           
  return -1