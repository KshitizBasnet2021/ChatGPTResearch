def lIlIIIlI(IIlllIIllllllIIll, lIIlIIlIllIlIllI):
  IIIIlllIll = 0
  lIIlIIllIllIlllIlIlI = len(IIlllIIllllllIIll)-1
  while IIIIlllIll <= lIIlIIllIllIlllIlIlI:
    lIlllIllIlIIlIIlI = (IIIIlllIll + lIIlIIllIllIlllIlIlI) // 2
    if lIIlIIlIllIlIllI == IIlllIIllllllIIll[lIlllIllIlIIlIIlI]:         
      return True
    elif lIIlIIlIllIlIllI > IIlllIIllllllIIll[lIlllIllIlIIlIIlI]:
      lIIlIIllIllIlllIlIlI = lIlllIllIlIIlIIlI - 1                
    else:
      IIIIlllIll = lIlllIllIlIIlIIlI + 1                 
  return False                      