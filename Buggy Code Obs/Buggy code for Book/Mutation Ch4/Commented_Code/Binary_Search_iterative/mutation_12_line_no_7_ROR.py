def lIllllIlllIlIlllIIlI(lIIllIllI, lIlIIIIIlIl):
  lIllIIIIIlII = 0
  lIllIllllllIl = len(lIIllIllI)-1
  while lIllIIIIIlII <= lIllIllllllIl:
    lIIIIlllllIlIllI = (lIllIIIIIlII + lIllIllllllIl) // 2
    if lIlIIIIIlIl != lIIllIllI[lIIIIlllllIlIllI]:
      return True
    elif lIlIIIIIlIl < lIIllIllI[lIIIIlllllIlIllI]:
      lIllIllllllIl = lIIIIlllllIlIllI - 1                
    else:
      lIllIIIIIlII = lIIIIlllllIlIllI + 1                 
  return False                      