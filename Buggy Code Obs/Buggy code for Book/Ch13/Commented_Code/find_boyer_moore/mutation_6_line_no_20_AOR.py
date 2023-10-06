def IlIIIlllllIIIl(lIIIlllIIIlIIIl, IlllllIll):
  llIllIlll, lIIIlIlllIl = len(lIIIlllIIIlIIIl), len(IlllllIll)                   
  if lIIIlIlllIl == 0: return 0                     
  lIIllllIllIIllIIlI = {}                               
  for lIlllllllIllIIIlIII in range(lIIIlIlllIl):
    lIIllllIllIIllIIlI[ IlllllIll[lIlllllllIllIIIlIII] ] = lIlllllllIllIIIlIII                      
  IIllIlIlIIIIllIIlI = lIIIlIlllIl-1                                 
  lIlllllllIllIIIlIII = lIIIlIlllIl-1                                 
  while IIllIlIlIIIIllIIlI < llIllIlll:
    if lIIIlllIIIlIIIl[IIllIlIlIIIIllIIlI] == IlllllIll[lIlllllllIllIIIlIII]:                      
      if lIlllllllIllIIIlIII == 0:
        return IIllIlIlIIIIllIIlI                          
      else:
        IIllIlIlIIIIllIIlI -= 1                            
        lIlllllllIllIIIlIII -= 1                            
    else:
      IIllIIIIl = lIIllllIllIIllIIlI.get(lIIIlllIIIlIIIl[IIllIlIlIIIIllIIlI], -1)              
      IIllIlIlIIIIllIIlI += lIIIlIlllIl + min(lIlllllllIllIIIlIII, IIllIIIIl + 1)
      lIlllllllIllIIIlIII = lIIIlIlllIl - 1                           
  return -1