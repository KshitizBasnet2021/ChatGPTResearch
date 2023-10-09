def IllIIllIII(lllIlIlIlIll, llIIlllIlIIlIIlIll):
  if llIIlllIlIIlIIlIll == 0:
    return 1
  else:
    lIIIlIIllI = IllIIllIII(lllIlIlIlIll, llIIlllIlIIlIIlIll // 2)          
    IllIllIIIlII = lIIIlIIllI * lIIIlIIllI
    if llIIlllIlIIlIIlIll % 2 == 1:                      
      IllIllIIIlII /= lllIlIlIlIll
    return IllIllIIIlII