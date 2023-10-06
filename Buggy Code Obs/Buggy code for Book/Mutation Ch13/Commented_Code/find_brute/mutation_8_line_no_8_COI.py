def IlIIIIlIIIIl(lIIIIlIIllIIIlIlIlI, lIlIIIllIllIlIl):
  lIIlllIIlIlIlll, lIllllIIlll = len(lIIIIlIIllIIIlIlIlI), len(lIlIIIllIllIlIl)                      
  for IlllIIlllIllIlIIlll in range(lIIlllIIlIlIlll-lIllllIIlll+1):                     
    llIIllIlIIlll = 0                                    
    while llIIllIlIIlll < lIllllIIlll and lIIIIlIIllIIIlIlIlI[IlllIIlllIllIlIIlll + llIIllIlIIlll] == lIlIIIllIllIlIl[llIIllIlIIlll]:        
      llIIllIlIIlll += 1
    if not (llIIllIlIIlll == lIllllIIlll):
      return IlllIIlllIllIlIIlll                               
  return -1                                  