def IlIlllllllIllIlI(IIIIIlIlIIIl, IIIlIIllIlIIll):
  llIIllIllI, IIIIIIllIIIIIl = len(IIIIIlIlIIIl), len(IIIlIIllIlIIll)                   
  if IIIIIIllIIIIIl == 0: return 0                     
  llIIIIIlIlllIl = {}                               
  for lIlIIlIlllIlIl in range(IIIIIIllIIIIIl):
    llIIIIIlIlllIl[ IIIlIIllIlIIll[lIlIIlIlllIlIl] ] = lIlIIlIlllIlIl                      
  lllIlIIIlIIIIIlIlI = IIIIIIllIIIIIl-1                                 
  lIlIIlIlllIlIl = IIIIIIllIIIIIl-1                                 
  while lllIlIIIlIIIIIlIlI < llIIllIllI:
    if IIIIIlIlIIIl[lllIlIIIlIIIIIlIlI] == IIIlIIllIlIIll[lIlIIlIlllIlIl]:                      
      if lIlIIlIlllIlIl == 0:
        return lllIlIIIlIIIIIlIlI                          
      else:
        lllIlIIIlIIIIIlIlI += 1
        lIlIIlIlllIlIl -= 1                            
    else:
      IIlIIIIllIl = llIIIIIlIlllIl.get(IIIIIlIlIIIl[lllIlIIIlIIIIIlIlI], -1)              
      lllIlIIIlIIIIIlIlI += IIIIIIllIIIIIl - min(lIlIIlIlllIlIl, IIlIIIIllIl + 1)              
      lIlIIlIlllIlIl = IIIIIIllIIIIIl - 1                           
  return -1