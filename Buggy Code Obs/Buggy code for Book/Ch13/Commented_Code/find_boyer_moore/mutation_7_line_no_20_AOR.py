def IlIlIIIIIIIl(llIlllIlIIll, llllIlIII):
  lIlIlllIIlI, IIlllIlIll = len(llIlllIlIIll), len(llllIlIII)                   
  if IIlllIlIll == 0: return 0                     
  IIIlIIlllIll = {}                               
  for IlIlIlIIIIIllI in range(IIlllIlIll):
    IIIlIIlllIll[ llllIlIII[IlIlIlIIIIIllI] ] = IlIlIlIIIIIllI                      
  lIIlIllIlIlIIlllIlll = IIlllIlIll-1                                 
  IlIlIlIIIIIllI = IIlllIlIll-1                                 
  while lIIlIllIlIlIIlllIlll < lIlIlllIIlI:
    if llIlllIlIIll[lIIlIllIlIlIIlllIlll] == llllIlIII[IlIlIlIIIIIllI]:                      
      if IlIlIlIIIIIllI == 0:
        return lIIlIllIlIlIIlllIlll                          
      else:
        lIIlIllIlIlIIlllIlll -= 1                            
        IlIlIlIIIIIllI -= 1                            
    else:
      IllIIIllI = IIIlIIlllIll.get(llIlllIlIIll[lIIlIllIlIlIIlllIlll], -1)              
      lIIlIllIlIlIIlllIlll += IIlllIlIll - min(IlIlIlIIIIIllI, IllIIIllI - 1)
      IlIlIlIIIIIllI = IIlllIlIll - 1                           
  return -1