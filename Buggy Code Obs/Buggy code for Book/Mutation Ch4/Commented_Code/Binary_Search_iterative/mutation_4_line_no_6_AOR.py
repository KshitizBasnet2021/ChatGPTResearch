def IlllIIllll(lIIIIIIIlIIlI, lIIIlIlIIlllIlII):
  lIlIlIIIIll = 0
  lllIllllIIIlllllIII = len(lIIIIIIIlIIlI)-1
  while lIlIlIIIIll <= lllIllllIIIlllllIII:
    IIllIIlIllIlII = (lIlIlIIIIll + lllIllllIIIlllllIII) * 2
    if lIIIlIlIIlllIlII == lIIIIIIIlIIlI[IIllIIlIllIlII]:         
      return True
    elif lIIIlIlIIlllIlII < lIIIIIIIlIIlI[IIllIIlIllIlII]:
      lllIllllIIIlllllIII = IIllIIlIllIlII - 1                
    else:
      lIlIlIIIIll = IIllIIlIllIlII + 1                 
  return False                      