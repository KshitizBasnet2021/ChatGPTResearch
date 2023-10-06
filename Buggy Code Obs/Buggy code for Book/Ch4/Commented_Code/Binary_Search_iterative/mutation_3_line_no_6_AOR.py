def IlIllIlIll(llllIIIIl, IIlllIIllI):
  lIllIIllIlIIIlIIllII = 0
  lllIIIlIlI = len(llllIIIIl)-1
  while lIllIIllIlIIIlIIllII <= lllIIIlIlI:
    lIlIIlllllllllllIlI = (lIllIIllIlIIIlIIllII + lllIIIlIlI) / 2
    if IIlllIIllI == llllIIIIl[lIlIIlllllllllllIlI]:         
      return True
    elif IIlllIIllI < llllIIIIl[lIlIIlllllllllllIlI]:
      lllIIIlIlI = lIlIIlllllllllllIlI - 1                
    else:
      lIllIIllIlIIIlIIllII = lIlIIlllllllllllIlI + 1                 
  return False                      