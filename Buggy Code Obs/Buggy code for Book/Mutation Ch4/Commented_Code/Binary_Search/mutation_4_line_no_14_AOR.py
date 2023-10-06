def IIlllIIIlll(llIIlIIIlII, lllllllllII, lllIIIlllIlI, llllIIllIlIIIl):
  if lllIIIlllIlI > llllIIllIlIIIl:
    return False                    
  else:
    IIIIlllIll = (lllIIIlllIlI + llllIIllIlIIIl) // 2
    if lllllllllII == llIIlIIIlII[IIIIlllIll]:         
      return True
    elif lllllllllII < llIIlIIIlII[IIIIlllIll]:
      return IIlllIIIlll(llIIlIIIlII, lllllllllII, lllIIIlllIlI, IIIIlllIll + 1)
    else:
      return IIlllIIIlll(llIIlIIIlII, lllllllllII, IIIIlllIll + 1, llllIIllIlIIIl)