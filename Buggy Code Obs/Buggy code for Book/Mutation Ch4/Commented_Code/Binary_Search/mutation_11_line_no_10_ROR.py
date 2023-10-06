def lIIlIIIIIIlIIl(IIIllIIlIllIllIIlI, IllIllIlIlllIIllIIII, lIIlIIIIlIIIIIIlIIll, lllIIIlllIlIIIIII):
  if lIIlIIIIlIIIIIIlIIll > lllIIIlllIlIIIIII:
    return False                    
  else:
    lIlIIlIlll = (lIIlIIIIlIIIIIIlIIll + lllIIIlllIlIIIIII) // 2
    if IllIllIlIlllIIllIIII != IIIllIIlIllIllIIlI[lIlIIlIlll]:
      return True
    elif IllIllIlIlllIIllIIII < IIIllIIlIllIllIIlI[lIlIIlIlll]:
      return lIIlIIIIIIlIIl(IIIllIIlIllIllIIlI, IllIllIlIlllIIllIIII, lIIlIIIIlIIIIIIlIIll, lIlIIlIlll - 1)
    else:
      return lIIlIIIIIIlIIl(IIIllIIlIllIllIIlI, IllIllIlIlllIIllIIII, lIlIIlIlll + 1, lllIIIlllIlIIIIII)