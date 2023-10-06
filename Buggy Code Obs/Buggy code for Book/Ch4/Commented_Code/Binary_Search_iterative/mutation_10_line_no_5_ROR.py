def llIIIIIlIlIIl(llIIIIllIlIIl, llIIIIIIlII):
  lIllllIIllllI = 0
  IIllIIIIIIl = len(llIIIIllIlIIl)-1
  while lIllllIIllllI >= IIllIIIIIIl:
    IIllIlllIIIIlllIlI = (lIllllIIllllI + IIllIIIIIIl) // 2
    if llIIIIIIlII == llIIIIllIlIIl[IIllIlllIIIIlllIlI]:         
      return True
    elif llIIIIIIlII < llIIIIllIlIIl[IIllIlllIIIIlllIlI]:
      IIllIIIIIIl = IIllIlllIIIIlllIlI - 1                
    else:
      lIllllIIllllI = IIllIlllIIIIlllIlI + 1                 
  return False                      