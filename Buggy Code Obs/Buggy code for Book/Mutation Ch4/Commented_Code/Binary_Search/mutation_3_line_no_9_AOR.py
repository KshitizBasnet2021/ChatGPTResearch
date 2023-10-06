def IllIIllIIIIllIl(llllIlllIIllllIIlI, IllllIllIlIllIlll, IIllIIlIlIIlII, llIllIIlllIIllllII):
  if IIllIIlIlIIlII > llIllIIlllIIllllII:
    return False                    
  else:
    IIIllIIIIlllIIllIll = (IIllIIlIlIIlII + llIllIIlllIIllllII) * 2
    if IllllIllIlIllIlll == llllIlllIIllllIIlI[IIIllIIIIlllIIllIll]:         
      return True
    elif IllllIllIlIllIlll < llllIlllIIllllIIlI[IIIllIIIIlllIIllIll]:
      return IllIIllIIIIllIl(llllIlllIIllllIIlI, IllllIllIlIllIlll, IIllIIlIlIIlII, IIIllIIIIlllIIllIll - 1)
    else:
      return IllIIllIIIIllIl(llllIlllIIllllIIlI, IllllIllIlIllIlll, IIIllIIIIlllIIllIll + 1, llIllIIlllIIllllII)