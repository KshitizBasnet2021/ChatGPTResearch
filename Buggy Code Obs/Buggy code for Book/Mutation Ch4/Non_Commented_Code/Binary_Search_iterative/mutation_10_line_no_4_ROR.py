def llIlIlIIl(IIlIlllllIIIlIllll, llllIIll):
  llllIllIlllIIIllIl = 0
  IlllIIlIlIlIllIIl = len(IIlIlllllIIIlIllll)-1
  while llllIllIlllIIIllIl >= IlllIIlIlIlIllIIl:
    lIIIllIIllIlIl = (llllIllIlllIIIllIl + IlllIIlIlIlIllIIl) // 2
    if llllIIll == IIlIlllllIIIlIllll[lIIIllIIllIlIl]:
      return True
    elif llllIIll < IIlIlllllIIIlIllll[lIIIllIIllIlIl]:
      IlllIIlIlIlIllIIl = lIIIllIIllIlIl - 1
    else:
      llllIllIlllIIIllIl = lIIIllIIllIlIl + 1
  return False