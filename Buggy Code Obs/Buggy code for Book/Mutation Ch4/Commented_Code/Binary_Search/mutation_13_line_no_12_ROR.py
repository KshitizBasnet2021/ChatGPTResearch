def IIllIlllll(IllIIIIllIlIlIlIIlI, IlllllllIlllIIIIII, lIllIlllIllll, IIlllllIIIllllII):
  if lIllIlllIllll > IIlllllIIIllllII:
    return False                    
  else:
    lIlIIIIIIIllI = (lIllIlllIllll + IIlllllIIIllllII) // 2
    if IlllllllIlllIIIIII == IllIIIIllIlIlIlIIlI[lIlIIIIIIIllI]:         
      return True
    elif IlllllllIlllIIIIII <= IllIIIIllIlIlIlIIlI[lIlIIIIIIIllI]:
      return IIllIlllll(IllIIIIllIlIlIlIIlI, IlllllllIlllIIIIII, lIllIlllIllll, lIlIIIIIIIllI - 1)
    else:
      return IIllIlllll(IllIIIIllIlIlIlIIlI, IlllllllIlllIIIIII, lIlIIIIIIIllI + 1, IIlllllIIIllllII)