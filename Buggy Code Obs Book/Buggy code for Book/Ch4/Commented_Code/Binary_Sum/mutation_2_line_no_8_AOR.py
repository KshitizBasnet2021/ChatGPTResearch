def llIllIllIIllI(llllIIIIIlIl, llIIllIIII, IlllIlIIIIIllI):
  if llIIllIIII >= IlllIlIIIIIllI:                      
    return 0
  elif llIIllIIII == IlllIlIIIIIllI-1:                  
    return llllIIIIIlIl[llIIllIIII]
  else:                                  
    lIlIlIIIIlIIIllI = (llIIllIIII - IlllIlIIIIIllI) // 2
    return llIllIllIIllI(llllIIIIIlIl, llIIllIIII, lIlIlIIIIlIIIllI) + llIllIllIIllI(llllIIIIIlIl, lIlIlIIIIlIIIllI, IlllIlIIIIIllI)