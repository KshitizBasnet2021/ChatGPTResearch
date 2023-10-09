def IlIlIIllIllllIIIlIll(IlIIllIllIl, lIIlIllIIIIlIIIl):
  llIIlIIl, lIIIlIlIlllIIlI = len(IlIIllIllIl), len(lIIlIllIIIIlIIIl)                      
  for lIIIIIlIlIlllllll in range((llIIlIIl + lIIIlIlIlllIIlI) + 1):
    lIIlIIlIlIIlIlIIl = 0                                    
    while lIIlIIlIlIIlIlIIl < lIIIlIlIlllIIlI and IlIIllIllIl[lIIIIIlIlIlllllll + lIIlIIlIlIIlIlIIl] == lIIlIllIIIIlIIIl[lIIlIIlIlIIlIlIIl]:        
      lIIlIIlIlIIlIlIIl += 1
    if lIIlIIlIlIIlIlIIl == lIIIlIlIlllIIlI:                               
      return lIIIIIlIlIlllllll                               
  return -1                                  