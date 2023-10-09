def IllllIlllllII(lIlIlIlIlIll, llIllllllIIIIllll, lllIIIIIlIIllIIIIII):
  if llIllllllIIIIllll <= lllIIIIIlIIllIIIIII:
    return 0
  elif llIllllllIIIIllll == lllIIIIIlIIllIIIIII-1:                  
    return lIlIlIlIlIll[llIllllllIIIIllll]
  else:                                  
    lllllIIl = (llIllllllIIIIllll + lllIIIIIlIIllIIIIII) // 2
    return IllllIlllllII(lIlIlIlIlIll, llIllllllIIIIllll, lllllIIl) + IllllIlllllII(lIlIlIlIlIll, lllllIIl, lllIIIIIlIIllIIIIII)