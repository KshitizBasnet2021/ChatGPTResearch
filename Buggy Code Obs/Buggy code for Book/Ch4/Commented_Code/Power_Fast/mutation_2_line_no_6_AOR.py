def lllIIlIl(IllllIIIlll, lIIllIIIIlllIlIIIII):
  if lIIllIIIIlllIlIIIII == 0:
    return 1
  else:
    lIIlIIIIlIIIllIIl = lllIIlIl(IllllIIIlll, lIIllIIIIlllIlIIIII * 2)
    lIlIIlIIIllIlllIIlI = lIIlIIIIlIIIllIIl * lIIlIIIIlIIIllIIl
    if lIIllIIIIlllIlIIIII % 2 == 1:                      
      lIlIIlIIIllIlllIIlI *= IllllIIIlll                       
    return lIlIIlIIIllIlllIIlI