def llllIIIIllIIllIII(lIIlIlIlII, lIlIIIlll):
  lIIlllllIl = 0
  IIllIIIIl = len(lIIlIlIlII)-1
  while lIIlllllIl <= IIllIIIIl:
    llllIIIlIIIIlllII = (lIIlllllIl + IIllIIIIl) // 2
    if lIlIIIlll == lIIlIlIlII[llllIIIlIIIIlllII]:         
      return True
    elif lIlIIIlll < lIIlIlIlII[llllIIIlIIIIlllII]:
      IIllIIIIl = llllIIIlIIIIlllII + 1
    else:
      lIIlllllIl = llllIIIlIIIIlllII + 1                 
  return False                      