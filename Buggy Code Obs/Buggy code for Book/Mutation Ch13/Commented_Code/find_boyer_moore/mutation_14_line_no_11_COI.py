def IIlIIllI(lIlIIIIIIllIlll, lIlIIllIIlIllI):
  lIIIIIlllIlIlIIIllll, IIIIIlllllIIIlIIlIll = len(lIlIIIIIIllIlll), len(lIlIIllIIlIllI)                   
  if IIIIIlllllIIIlIIlIll == 0: return 0                     
  IlIIIIIIIllIllIIIll = {}                               
  for IIIIllIIIll in range(IIIIIlllllIIIlIIlIll):
    IlIIIIIIIllIllIIIll[ lIlIIllIIlIllI[IIIIllIIIll] ] = IIIIllIIIll                      
  IIlIlllllIIlllIlI = IIIIIlllllIIIlIIlIll-1                                 
  IIIIllIIIll = IIIIIlllllIIIlIIlIll-1                                 
  while not (IIlIlllllIIlllIlI < lIIIIIlllIlIlIIIllll):
    if lIlIIIIIIllIlll[IIlIlllllIIlllIlI] == lIlIIllIIlIllI[IIIIllIIIll]:                      
      if IIIIllIIIll == 0:
        return IIlIlllllIIlllIlI                          
      else:
        IIlIlllllIIlllIlI -= 1                            
        IIIIllIIIll -= 1                            
    else:
      IllllIIlIIllI = IlIIIIIIIllIllIIIll.get(lIlIIIIIIllIlll[IIlIlllllIIlllIlI], -1)              
      IIlIlllllIIlllIlI += IIIIIlllllIIIlIIlIll - min(IIIIllIIIll, IllllIIlIIllI + 1)              
      IIIIllIIIll = IIIIIlllllIIIlIIlIll - 1                           
  return -1