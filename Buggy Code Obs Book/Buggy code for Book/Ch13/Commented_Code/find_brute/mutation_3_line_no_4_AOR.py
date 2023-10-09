def IIIIlIIllIIlIIlIIIII(lIIIIIIllll, IlIlllIllII):
  lIlIlllIIll, IIIIIIIIlI = len(lIIIIIIllll), len(IlIlllIllII)                      
  for llIIIIlIlIlIIlllllll in range((lIlIlllIIll - IIIIIIIIlI) - 1):
    lIllllIlIIIIlllI = 0                                    
    while lIllllIlIIIIlllI < IIIIIIIIlI and lIIIIIIllll[llIIIIlIlIlIIlllllll + lIllllIlIIIIlllI] == IlIlllIllII[lIllllIlIIIIlllI]:        
      lIllllIlIIIIlllI += 1
    if lIllllIlIIIIlllI == IIIIIIIIlI:                               
      return llIIIIlIlIlIIlllllll                               
  return -1                                  