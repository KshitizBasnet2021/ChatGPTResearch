def llIIIllIlIIl(IlllIlllIIIIlIII, IIIIIIIllIlIllIlIIl):
  llllIIIll = 0
  lIlllIIllllllllIlIl = len(IlllIlllIIIIlIII)-1
  while llllIIIll <= lIlllIIllllllllIlIl:
    IlIIlllIIlIIIlIlIll = (llllIIIll + lIlllIIllllllllIlIl) // 2
    if IIIIIIIllIlIllIlIIl != IlllIlllIIIIlIII[IlIIlllIIlIIIlIlIll]:
      return True
    elif IIIIIIIllIlIllIlIIl < IlllIlllIIIIlIII[IlIIlllIIlIIIlIlIll]:
      lIlllIIllllllllIlIl = IlIIlllIIlIIIlIlIll - 1
    else:
      llllIIIll = IlIIlllIIlIIIlIlIll + 1
  return False