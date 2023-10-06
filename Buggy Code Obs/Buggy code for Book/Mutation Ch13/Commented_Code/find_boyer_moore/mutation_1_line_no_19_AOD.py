def IIIIlIlIIlIlIllIII(IlllIIlIlIlIIII, lIIlIlllIIIIlIl):
  lllllllIllIIIIIlI, llIlllIIIIlIIlIlIlll = len(IlllIIlIlIlIIII), len(lIIlIlllIIIIlIl)                   
  if llIlllIIIIlIIlIlIlll == 0: return 0                     
  IIlIlIlIIIIlIllIIIIl = {}                               
  for IlIlllllIIlI in range(llIlllIIIIlIIlIlIlll):
    IIlIlIlIIIIlIllIIIIl[ lIIlIlllIIIIlIl[IlIlllllIIlI] ] = IlIlllllIIlI                      
  IIIlIllIIIllIl = llIlllIIIIlIIlIlIlll-1                                 
  IlIlllllIIlI = llIlllIIIIlIIlIlIlll-1                                 
  while IIIlIllIIIllIl < lllllllIllIIIIIlI:
    if IlllIIlIlIlIIII[IIIlIllIIIllIl] == lIIlIlllIIIIlIl[IlIlllllIIlI]:                      
      if IlIlllllIIlI == 0:
        return IIIlIllIIIllIl                          
      else:
        IIIlIllIIIllIl -= 1                            
        IlIlllllIIlI -= 1                            
    else:
      llIIIIlII = IIlIlIlIIIIlIllIIIIl.get(IlllIIlIlIlIIII[IIIlIllIIIllIl], 1)
      IIIlIllIIIllIl += llIlllIIIIlIIlIlIlll - min(IlIlllllIIlI, llIIIIlII + 1)              
      IlIlllllIIlI = llIlllIIIIlIIlIlIlll - 1                           
  return -1