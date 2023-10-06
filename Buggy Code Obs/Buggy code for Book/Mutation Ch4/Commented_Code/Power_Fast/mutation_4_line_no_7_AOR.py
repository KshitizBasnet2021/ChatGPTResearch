def lIIIIlllIlIIIIllI(llIIllIllll, lIIIIIIl):
  if lIIIIIIl == 0:
    return 1
  else:
    lIllIlIlIl = lIIIIlllIlIIIIllI(llIIllIllll, lIIIIIIl // 2)          
    IlllIIIIlllIlll = lIllIlIlIl // lIllIlIlIl
    if lIIIIIIl % 2 == 1:                      
      IlllIIIIlllIlll *= llIIllIllll                       
    return IlllIIIIlllIlll