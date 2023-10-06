def IlIlIllIlIlIIlIII(llIIIlllIIIlIll, llIlIlIllllIIIIlII):
  if llIlIlIllllIIIIlII == 0:
    return 1
  else:
    lIIIlllIIllIlllIIlII = IlIlIllIlIlIIlIII(llIIIlllIIIlIll, llIlIlIllllIIIIlII / 2)
    llIlIIlIlIII = lIIIlllIIllIlllIIlII * lIIIlllIIllIlllIIlII
    if llIlIlIllllIIIIlII % 2 == 1:
      llIlIIlIlIII *= llIIIlllIIIlIll                       
    return llIlIIlIlIII