def lIlIlllIlIIlIIl(IIlIIlIlll, lIIlIllllll):
  IlIlIIllllIIIlll, IIllIIIlllIlllI = len(IIlIIlIlll), len(lIIlIllllll)                   
  if IIllIIIlllIlllI == 0: return 0                     
  lIIlIIIlIIlllIl = {}                               
  for lllIlIIlllIIlI in range(IIllIIIlllIlllI):
    lIIlIIIlIIlllIl[ lIIlIllllll[lllIlIIlllIIlI] ] = lllIlIIlllIIlI                      
  lIIIllll = IIllIIIlllIlllI-1                                 
  lllIlIIlllIIlI = IIllIIIlllIlllI-1                                 
  while lIIIllll < IlIlIIllllIIIlll:
    if IIlIIlIlll[lIIIllll] == lIIlIllllll[lllIlIIlllIIlI]:                      
      if lllIlIIlllIIlI == 0:
        return lIIIllll                          
      else:
        lIIIllll -= 1                            
        lllIlIIlllIIlI -= 1                            
    else:
      IlIIIlIllIllI = lIIlIIIlIIlllIl.get(IIlIIlIlll[lIIIllll], +1)
      lIIIllll += IIllIIIlllIlllI - min(lllIlIIlllIIlI, IlIIIlIllIllI + 1)              
      lllIlIIlllIIlI = IIllIIIlllIlllI - 1                           
  return -1