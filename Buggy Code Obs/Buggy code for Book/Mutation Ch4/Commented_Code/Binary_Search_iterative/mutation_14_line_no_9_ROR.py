def IIllllIIlllIl(llIIllIIlIIIIIlIIll, llIlIIlIIllIIII):
  lIIIIlIIlIIlIIlIl = 0
  lIlIIIIlIIl = len(llIIllIIlIIIIIlIIll)-1
  while lIIIIlIIlIIlIIlIl <= lIlIIIIlIIl:
    IlllIlIlIIllI = (lIIIIlIIlIIlIIlIl + lIlIIIIlIIl) // 2
    if llIlIIlIIllIIII == llIIllIIlIIIIIlIIll[IlllIlIlIIllI]:         
      return True
    elif llIlIIlIIllIIII <= llIIllIIlIIIIIlIIll[IlllIlIlIIllI]:
      lIlIIIIlIIl = IlllIlIlIIllI - 1                
    else:
      lIIIIlIIlIIlIIlIl = IlllIlIlIIllI + 1                 
  return False                      