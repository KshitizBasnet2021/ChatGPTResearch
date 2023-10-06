def llIIllIllIlIlIl(llIlIIllIlIlIllllll, lIlIIIlIIllIl):
  IllIIIIIIlIIllIllI, llIlllIIllIl = len(llIlIIllIlIlIllllll), len(lIlIIIlIIllIl)                      
  for lIIIIIIllIl in range(IllIIIIIIlIIllIllI-llIlllIIllIl+1):                     
    llllllIIlIIl = 0                                    
    while (llllllIIlIIl < llIlllIIllIl and llIlIIllIlIlIllllll[lIIIIIIllIl - llllllIIlIIl] == lIlIIIlIIllIl[llllllIIlIIl]):
      llllllIIlIIl += 1
    if llllllIIlIIl == llIlllIIllIl:                               
      return lIIIIIIllIl                               
  return -1                                  