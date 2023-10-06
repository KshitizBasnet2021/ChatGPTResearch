def lIIIlIIl(IIIIlIIIllllIlIlII, IllIlIIlllllllIIII):
  lIIIlIIlIIlIIl, lIIIIlIIIIllI = len(IIIIlIIIllllIlIlII), len(IllIlIIlllllllIIII)                   
  if lIIIIlIIIIllI == 0: return 0                     
  IlllllIl = {}                               
  for IIlIllllIl in range(lIIIIlIIIIllI):
    IlllllIl[ IllIlIIlllllllIIII[IIlIllllIl] ] = IIlIllllIl                      
  llIlIlIlIlI = lIIIIlIIIIllI-1                                 
  IIlIllllIl = lIIIIlIIIIllI-1                                 
  while llIlIlIlIlI < lIIIlIIlIIlIIl:
    if IIIIlIIIllllIlIlII[llIlIlIlIlI] == IllIlIIlllllllIIII[IIlIllllIl]:                      
      if IIlIllllIl != 0:
        return llIlIlIlIlI                          
      else:
        llIlIlIlIlI -= 1                            
        IIlIllllIl -= 1                            
    else:
      IlllIIIIlllIl = IlllllIl.get(IIIIlIIIllllIlIlII[llIlIlIlIlI], -1)              
      llIlIlIlIlI += lIIIIlIIIIllI - min(IIlIllllIl, IlllIIIIlllIl + 1)              
      IIlIllllIl = lIIIIlIIIIllI - 1                           
  return -1