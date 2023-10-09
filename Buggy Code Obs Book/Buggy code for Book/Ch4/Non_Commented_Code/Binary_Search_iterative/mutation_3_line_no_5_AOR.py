def IIIIIIllllllllIlIIlI(IIllllIII, lIlllIIlIlllIIIll):
  llIlIlllllIIl = 0
  lIlIIllII = len(IIllllIII)-1
  while llIlIlllllIIl <= lIlIIllII:
    lIIlIIll = (llIlIlllllIIl + lIlIIllII) / 2
    if lIlllIIlIlllIIIll == IIllllIII[lIIlIIll]:
      return True
    elif lIlllIIlIlllIIIll < IIllllIII[lIIlIIll]:
      lIlIIllII = lIIlIIll - 1
    else:
      llIlIlllllIIl = lIIlIIll + 1
  return False