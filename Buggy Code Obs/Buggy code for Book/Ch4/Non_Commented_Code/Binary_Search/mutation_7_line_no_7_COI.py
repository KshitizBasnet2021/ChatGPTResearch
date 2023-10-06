def IlIIIIIIIllIIl(IIlIlIIII, IllIlllIlllIIlIIllll, lllIIIlIllIlllIlIlII, IllIlIIlllllIllI):
  if lllIIIlIllIlllIlIlII > IllIlIIlllllIllI:
    return False
  else:
    lIIIllIIIlIIIllIlll = (lllIIIlIllIlllIlIlII + IllIlIIlllllIllI) // 2
    if not (IllIlllIlllIIlIIllll == IIlIlIIII[lIIIllIIIlIIIllIlll]):
      return True
    elif IllIlllIlllIIlIIllll < IIlIlIIII[lIIIllIIIlIIIllIlll]:
      return IlIIIIIIIllIIl(IIlIlIIII, IllIlllIlllIIlIIllll, lllIIIlIllIlllIlIlII, lIIIllIIIlIIIllIlll - 1)
    else:
      return IlIIIIIIIllIIl(IIlIlIIII, IllIlllIlllIIlIIllll, lIIIllIIIlIIIllIlll + 1, IllIlIIlllllIllI)