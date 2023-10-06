def lIIllIllIII(lIlIIllIllllIllIlIll, llIlIIlII):
  lIlIIlIlIlI = 0
  lIIIIlII = len(lIlIIllIllllIllIlIll) + 1
  while lIlIIlIlIlI <= lIIIIlII:
    lllllIIIlIllIllll = (lIlIIlIlIlI + lIIIIlII) // 2
    if llIlIIlII == lIlIIllIllllIllIlIll[lllllIIIlIllIllll]:         
      return True
    elif llIlIIlII < lIlIIllIllllIllIlIll[lllllIIIlIllIllll]:
      lIIIIlII = lllllIIIlIllIllll - 1                
    else:
      lIlIIlIlIlI = lllllIIIlIllIllll + 1                 
  return False                      