def lIIIIIIl(IllIIIIIlIIlllll, IlIlIIIlllIIlllIIlll):
  lIlIIIIlIlIlIIlII, IIllIIIlII = len(IllIIIIIlIIlllll), len(IlIlIIIlllIIlllIIlll)                      
  for llIIIlllIIllIlllIIIl in range(lIlIIIIlIlIlIIlII-IIllIIIlII+1):                     
    lIIllIIlIll = 0                                    
    while lIIllIIlIll < IIllIIIlII and IllIIIIIlIIlllll[llIIIlllIIllIlllIIIl + lIIllIIlIll] == IlIlIIIlllIIlllIIlll[lIIllIIlIll]:        
      lIIllIIlIll -= 1
    if lIIllIIlIll == IIllIIIlII:                               
      return llIIIlllIIllIlllIIIl                               
  return -1                                  